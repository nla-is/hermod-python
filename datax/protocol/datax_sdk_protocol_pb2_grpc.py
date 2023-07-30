# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import datax_sdk_protocol_pb2 as datax__sdk__protocol__pb2


class DataXStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Initialize = channel.unary_unary(
                '/datax.sdk.protocol.v2.DataX/Initialize',
                request_serializer=datax__sdk__protocol__pb2.Settings.SerializeToString,
                response_deserializer=datax__sdk__protocol__pb2.Initialization.FromString,
                )
        self.Next = channel.unary_unary(
                '/datax.sdk.protocol.v2.DataX/Next',
                request_serializer=datax__sdk__protocol__pb2.NextOptions.SerializeToString,
                response_deserializer=datax__sdk__protocol__pb2.NextMessage.FromString,
                )
        self.Emit = channel.unary_unary(
                '/datax.sdk.protocol.v2.DataX/Emit',
                request_serializer=datax__sdk__protocol__pb2.EmitMessage.SerializeToString,
                response_deserializer=datax__sdk__protocol__pb2.EmitResult.FromString,
                )
        self.GetRequest = channel.unary_unary(
                '/datax.sdk.protocol.v2.DataX/GetRequest',
                request_serializer=datax__sdk__protocol__pb2.GetRequestOptions.SerializeToString,
                response_deserializer=datax__sdk__protocol__pb2.Request.FromString,
                )
        self.ReplyRequest = channel.unary_unary(
                '/datax.sdk.protocol.v2.DataX/ReplyRequest',
                request_serializer=datax__sdk__protocol__pb2.Reply.SerializeToString,
                response_deserializer=datax__sdk__protocol__pb2.ReplyResult.FromString,
                )
        self.SubmitRequest = channel.unary_unary(
                '/datax.sdk.protocol.v2.DataX/SubmitRequest',
                request_serializer=datax__sdk__protocol__pb2.Request.SerializeToString,
                response_deserializer=datax__sdk__protocol__pb2.Reply.FromString,
                )


class DataXServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Initialize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Next(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Emit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRequest(self, request, context):
        """Backend API
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplyRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitRequest(self, request, context):
        """Backend client API
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataXServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Initialize': grpc.unary_unary_rpc_method_handler(
                    servicer.Initialize,
                    request_deserializer=datax__sdk__protocol__pb2.Settings.FromString,
                    response_serializer=datax__sdk__protocol__pb2.Initialization.SerializeToString,
            ),
            'Next': grpc.unary_unary_rpc_method_handler(
                    servicer.Next,
                    request_deserializer=datax__sdk__protocol__pb2.NextOptions.FromString,
                    response_serializer=datax__sdk__protocol__pb2.NextMessage.SerializeToString,
            ),
            'Emit': grpc.unary_unary_rpc_method_handler(
                    servicer.Emit,
                    request_deserializer=datax__sdk__protocol__pb2.EmitMessage.FromString,
                    response_serializer=datax__sdk__protocol__pb2.EmitResult.SerializeToString,
            ),
            'GetRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRequest,
                    request_deserializer=datax__sdk__protocol__pb2.GetRequestOptions.FromString,
                    response_serializer=datax__sdk__protocol__pb2.Request.SerializeToString,
            ),
            'ReplyRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplyRequest,
                    request_deserializer=datax__sdk__protocol__pb2.Reply.FromString,
                    response_serializer=datax__sdk__protocol__pb2.ReplyResult.SerializeToString,
            ),
            'SubmitRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitRequest,
                    request_deserializer=datax__sdk__protocol__pb2.Request.FromString,
                    response_serializer=datax__sdk__protocol__pb2.Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'datax.sdk.protocol.v2.DataX', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataX(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Initialize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/datax.sdk.protocol.v2.DataX/Initialize',
            datax__sdk__protocol__pb2.Settings.SerializeToString,
            datax__sdk__protocol__pb2.Initialization.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Next(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/datax.sdk.protocol.v2.DataX/Next',
            datax__sdk__protocol__pb2.NextOptions.SerializeToString,
            datax__sdk__protocol__pb2.NextMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Emit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/datax.sdk.protocol.v2.DataX/Emit',
            datax__sdk__protocol__pb2.EmitMessage.SerializeToString,
            datax__sdk__protocol__pb2.EmitResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/datax.sdk.protocol.v2.DataX/GetRequest',
            datax__sdk__protocol__pb2.GetRequestOptions.SerializeToString,
            datax__sdk__protocol__pb2.Request.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplyRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/datax.sdk.protocol.v2.DataX/ReplyRequest',
            datax__sdk__protocol__pb2.Reply.SerializeToString,
            datax__sdk__protocol__pb2.ReplyResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubmitRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/datax.sdk.protocol.v2.DataX/SubmitRequest',
            datax__sdk__protocol__pb2.Request.SerializeToString,
            datax__sdk__protocol__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
