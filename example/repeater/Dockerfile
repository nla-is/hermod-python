FROM alpine:3.17

RUN apk add --no-cache python3

RUN apk add --no-cache py3-pip git && \
    pip3 install git+https://github.com/nla-is/datax-python.git@v1.0.0 && \
    apk del git

COPY repeater.py /

ENTRYPOINT ["python3", "/repeater.py"]
