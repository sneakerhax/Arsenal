FROM --platform=linux/x86_64 python:alpine

RUN apk -U upgrade && apk add bash wget unzip libc6-compat
RUN mkdir PyDNSRecon
COPY PyDNSRecon.py /PyDNSRecon/PyDNSRecon.py
WORKDIR /PyDNSRecon
RUN wget https://github.com/OWASP/Amass/releases/latest/download/amass_linux_arm64.zip && unzip amass_linux_arm64.zip && mv amass_linux_arm64.zip amass
RUN python -m pip install requests

ENTRYPOINT ["python", "PyDNSRecon.py"]
