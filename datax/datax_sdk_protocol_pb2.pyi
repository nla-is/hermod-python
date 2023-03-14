from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EmitMessage(_message.Message):
    __slots__ = ["data", "reference"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    reference: str
    def __init__(self, data: _Optional[bytes] = ..., reference: _Optional[str] = ...) -> None: ...

class EmitResult(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Initialization(_message.Message):
    __slots__ = ["configuration"]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    configuration: _struct_pb2.Struct
    def __init__(self, configuration: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class NextMessage(_message.Message):
    __slots__ = ["data", "reference", "stream"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    reference: str
    stream: str
    def __init__(self, reference: _Optional[str] = ..., stream: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class NextOptions(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Settings(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
