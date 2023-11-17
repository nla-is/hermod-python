FROM python:3.10-bookworm

RUN pip3 install git+https://github.com/nla-is/datax-python.git@v2.0.0-alpha.14

COPY driver.py /

ENTRYPOINT ["python3", "-u", "driver.py"]
