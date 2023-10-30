from ctypes import *
import cbor2
import json
import os


class DataX:
    def __init__(self, ):
        self._handle = cdll.LoadLibrary("libdatax-sdk.so")
        self._handle.datax_sdk_v2_initialize()
        self._handle.datax_sdk_v2_next.restype = c_size_t
        self._handle.datax_sdk_v2_emit.argtypes = [c_void_p, c_int32, c_char_p]
        self._handle.datax_sdk_v2_message_stream.restype = c_char_p
        self._handle.datax_sdk_v2_message_reference.restype = c_char_p
        self._handle.datax_sdk_v2_message_data.restype = c_void_p
        self._handle.datax_sdk_v2_message_data_size.restype = c_int32

    @staticmethod
    def get_configuration() -> dict:
        configuration_path = os.getenv('DATAX_CONFIGURATION')
        if configuration_path is None or configuration_path == '':
            configuration_path = "/datax/configuration"
        with open(configuration_path, 'r') as f:
            return json.load(f)

    # stream, reference, data
    def next(self) -> (str, str, dict):
        msg = self._handle.datax_sdk_v2_next()
        stream = self._handle.datax_sdk_v2_message_stream(msg)
        reference = self._handle.datax_sdk_v2_message_reference(msg)
        data = self._handle.datax_sdk_v2_message_data(msg)
        data_size = self._handle.datax_sdk_v2_message_data_size(msg)
        data = bytearray(string_at(data, data_size))
        data = cbor2.loads(data)
        self._handle.datax_sdk_v2_message_close(msg)
        return stream, reference, data

    def emit(self, message: dict, reference: str = None):
        if reference is None:
            reference = ""
        data = cbor2.dumps(message)
        self._handle.datax_sdk_v2_emit(data, len(data), reference)

