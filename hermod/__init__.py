from ctypes import *
from typing import Callable
import cbor2


def run(handler: Callable[[dict], dict]):
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
