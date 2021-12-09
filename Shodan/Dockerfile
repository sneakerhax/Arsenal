FROM python:alpine

RUN apk -U upgrade
RUN python -m pip install shodan
ARG shodan_api_key=shodan_api_key
RUN shodan init $shodan_api_key
ENTRYPOINT [ "shodan" ]
