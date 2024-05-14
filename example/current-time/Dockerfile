FROM python:3.10-bookworm

RUN pip3 install git+https://github.com/nla-is/hermod-python.git

COPY current_time.py /

ENTRYPOINT ["python3", "-u", "current_time.py"]
