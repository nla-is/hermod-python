FROM python:3.10-bookworm

RUN pip3 install git+https://github.com/nla-is/hermod-python.git

COPY repeater.py /

ENTRYPOINT ["python3", "-u", "/repeater.py"]
