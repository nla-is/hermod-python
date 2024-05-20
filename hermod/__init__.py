import os.path
import sys
from ctypes import *
from typing import Callable
import cbor2
import inspect


_SLEIPNIR_PATH = os.path.join('__sleipnir__', 'sleipnir.so')


def run(handler: Callable[..., dict]):
    if os.path.exists(_SLEIPNIR_PATH):
        _run_production(handler)
    else:
        _run_testing(handler)


def _run_production(handler: Callable[..., dict]):
    sleipnir = cdll.LoadLibrary("sleipnir.so")
    sleipnir.HermodV1ResultSetError.argtypes = [c_void_p, c_char_p]
    sleipnir.HermodV1ResultSetOutput.argtypes = [c_void_p, c_void_p, c_int32]

    hermod_v1_handler = CFUNCTYPE(c_void_p, c_void_p, c_void_p, c_int32)

    def callback(result, payload, payload_size):
        msg = cbor2.loads(bytearray(string_at(payload, payload_size)))
        try:
            data = cbor2.dumps(handler(msg))
            sleipnir.HermodV1ResultSetOutput(result, data, len(data))
        except Exception as e:
            sleipnir.HermodV1ResultSetError(result, bytes(f"exception {e}", encoding='ascii'))

    sleipnir.HermodV1Run(hermod_v1_handler(callback))


def _run_testing(handler: Callable[..., dict]):
    hr = HandlerRunner(handler)
    while True:
        print(hr.call_handler({'x': 23, 't': 12, 'xx': 101}))
        sys.exit(-1)


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
