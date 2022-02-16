# A dockerized version of the tool emailharvester by maldevel

FROM python:3.11.0a5-alpine3.15

RUN apk -U upgrade && apk add git
RUN git clone https://github.com/maldevel/EmailHarvester
WORKDIR /EmailHarvester
RUN pip install -r requirements.txt

WORKDIR /EmailHarvester
ENTRYPOINT ["python", "EmailHarvester.py"]
