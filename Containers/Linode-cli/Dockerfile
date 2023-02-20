FROM python:3-slim

RUN pip install --upgrade pip && pip3 install linode-cli --upgrade && pip3 install boto
ENTRYPOINT ["linode-cli"]
