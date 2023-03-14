import grpc
import json
import os
import msgpack
from datax import datax_sdk_protocol_pb2, datax_sdk_protocol_pb2_grpc


class DataX:
    def __init__(self,):
        sidecar_address = os.getenv("DATAX_SIDECAR_ADDRESS", "127.0.0.1:20001")
        self.channel = grpc.insecure_channel(sidecar_address)
        self.stub = datax_sdk_protocol_pb2_grpc.DataXStub(self.channel)

    @staticmethod
    def get_configuration():
        configuration_path = os.getenv('DATAX_CONFIGURATION')
        if configuration_path is None or configuration_path == '':
            configuration_path = "/datax/configuration"
        with open(configuration_path, 'r') as f:
            return json.load(f)

    def next(self):
        response = self.stub.Next(datax_sdk_protocol_pb2.NextOptions())
        msg = response.message
        return msg.stream, msg.reference, msgpack.unpackb(msg.data)

    def emit(self, message, reference=None):
        request = datax_sdk_protocol_pb2.EmitRequest(data=msgpack.packb(message))
        if reference is None:
            request.reference = reference
        self.stub.Emit(request)
