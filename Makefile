.PHONY: all generate

all:
	@echo "Nothing to be done"

generate: datax-sdk-protocol/v1/datax-sdk-protocol.proto
	python3 -m grpc_tools.protoc -Idatax-sdk-protocol/v1 --python_out=datax --grpc_python_out=datax datax-sdk-protocol/v1/datax-sdk-protocol.proto
