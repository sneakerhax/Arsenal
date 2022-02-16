# A dockerized version of the tool pyfiscan by fgeek

FROM python:3.11.0a5-alpine3.15

RUN apk -U upgrade && apk add git
RUN git clone https://github.com/fgeek/pyfiscan.git && cd pyfiscan
RUN pip3 install -r pyfiscan/requirements.lst
WORKDIR /pyfiscan

ENTRYPOINT ["python", "pyfiscan.py"]
