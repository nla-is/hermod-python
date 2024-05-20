import json
import os.path
import re
from typing import Callable
import inspect

_SLEIPNIR_PATH = '/__sleipnir__/sleipnir.so'


def run(handler: Callable[..., dict]):
    hr = HandlerRunner(handler)
    if os.path.exists(_SLEIPNIR_PATH):
        _run_production(hr)
    else:
        _run_testing(hr)


def _run_production(hr: 'HandlerRunner'):
    from ctypes import cdll, c_void_p, c_char_p, c_int32, CFUNCTYPE, string_at
    import cbor2

    sleipnir = cdll.LoadLibrary("sleipnir.so")
    sleipnir.HermodV1ResultSetError.argtypes = [c_void_p, c_char_p]
    sleipnir.HermodV1ResultSetOutput.argtypes = [c_void_p, c_void_p, c_int32]

    hermod_v1_handler = CFUNCTYPE(c_void_p, c_void_p, c_void_p, c_int32)

    def callback(result_ptr, payload, payload_size):
        try:
            params = cbor2.loads(bytearray(string_at(payload, payload_size)))
            result = hr.call_handler(params)
            data = cbor2.dumps(result)
            sleipnir.HermodV1ResultSetOutput(result_ptr, data, len(data))
        except Exception as e:
            sleipnir.HermodV1ResultSetError(result_ptr, bytes(f"exception {e}", encoding='ascii'))

    sleipnir.HermodV1Run(hermod_v1_handler(callback))


def _run_testing(hr: 'HandlerRunner'):
    import socket
    import multipart
    from wsgiref.simple_server import WSGIServer, WSGIRequestHandler, make_server

    def app(environ, start_response):
        content_type = environ.get('CONTENT_TYPE')
        if not content_type.startswith('multipart/form-data'):
            start_response('400 Bad Request', [])
            return ["expected multipart/form-data".encode("utf-8")]
        forms, files = multipart.parse_form_data(environ)
        params = {}
        if 'input.json' in forms:
            try:
                params = json.loads(forms['input.json'])
            except json.JSONDecodeError as e:
                start_response('400 Bad Request', [])
                return [f"invalid input {e}".encode("utf-8")]
        for file in files:
            params[file] = files[file].raw

        try:
            response = hr.call_handler(params)
        except Exception as e:
            start_response('400 Bad Request', [])
            return [f"exception {e}".encode("utf-8")]

        try:
            response = json.dumps(response)
        except Exception as e:
            start_response('500 Internal Server Error', [])
            return [f"exception {e}".encode("utf-8")]

        status = '200 OK'
        headers = [('Content-type', 'application/json; charset=utf-8')]

        start_response(status, headers)

        return [response.encode("utf-8")]

    class Handler(WSGIRequestHandler):
        def __init__(self, x, y, z):
            super().__init__(x, y, z)

        def address_string(self):
            if self.client_address is None or self.client_address == '':
                self.client_address = ('127.0.0.1', 0)
            return self.client_address[0]

    class Server(WSGIServer):
        def __init__(self, address, h=WSGIRequestHandler):
            self._address = address
            super().__init__(None, Handler)
            self.set_app(app)

        def server_bind(self):
            self.server_name = 'hermod'
            self.server_port = 666
            if self._address.startswith('/'):
                self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                if os.path.exists(self._address):
                    os.unlink(self._address)
                self.socket.bind(self._address)
                self.pretty_address = f"UNIX socket {self._address}"
            else:
                host, port = self._address.split(':')
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.socket.bind((host, int(port)))
                self.pretty_address = f"http://{host}:{port}"
            self.socket.listen(5)
            self.setup_environ()


    server_address = os.getenv('HERMOD_TESTING_SERVER_ADDRESS', '127.0.0.1:6660')
    server_address = re.sub('^http://', '', server_address)
    server = Server(server_address)
    print(f"Hermod - Starting testing server on {server.pretty_address} ...")
    server.serve_forever()


class HandlerRunner:
    def __init__(self, handler: Callable[..., dict]):
        self._handler = handler
        self._signature = inspect.signature(self._handler)
        self.call_handler = self._call_handler
        self._check_handler_validity()

    def _check_handler_validity(self):
        if not self._signature.return_annotation == dict:
            raise TypeError(f"handler signature must return dict type")
        if len(self._signature.parameters) == 1:
            parameter_name = next(iter(self._signature.parameters))
            p = self._signature.parameters[parameter_name]
            if p.kind == p.VAR_KEYWORD:
                self.call_handler = self._var_parameters_call_handler
                return
        for parameter_name in self._signature.parameters:
            p = self._signature.parameters[parameter_name]
            if p.kind in (p.VAR_KEYWORD, p.VAR_POSITIONAL):
                raise TypeError(f"{p.kind.description} parameter ('{parameter_name}') not supported in handler")

    def _var_parameters_call_handler(self, params: dict) -> dict:
        return self._handler(**params)

    def _call_handler(self, params: dict) -> dict:
        parameters = {}
        for parameter_name in self._signature.parameters:
            p = self._signature.parameters[parameter_name]
            if parameter_name in params:
                parameters[parameter_name] = params[parameter_name]
                del params[parameter_name]
            elif p.default == inspect.Parameter.empty:
                raise TypeError(f"handler has no default parameter {parameter_name}")
        bound_arguments = self._signature.bind(**parameters)
        bound_arguments.apply_defaults()
        return self._handler(**bound_arguments.arguments)
