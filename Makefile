.PHONY: all generate

all:
	@echo "Nothing to be done"

generate: datax-sdk-protocol/v2/datax-sdk-protocol.proto
	python3 -m grpc_tools.protoc -Idatax-sdk-protocol/v2 --python_out=datax/protocol --grpc_python_out=datax/protocol --pyi_out=datax/protocol datax-sdk-protocol/v2/datax-sdk-protocol.proto
