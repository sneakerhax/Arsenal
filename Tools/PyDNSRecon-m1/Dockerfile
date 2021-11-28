FROM --platform=linux/arm64/v8 python:3

RUN apt update && apt upgrade -y
RUN mkdir PyDNSRecon
COPY PyDNSRecon.py /PyDNSRecon
WORKDIR /PyDNSRecon
RUN wget https://github.com/OWASP/Amass/releases/latest/download/amass_linux_arm64.zip && unzip amass_linux_arm64.zip && mv amass_linux_arm64.zip amass
RUN wget https://opendata.rapid7.com/sonar.fdns_v2/2021-09-24-1632523752-fdns_cname.json.gz && mv 2021-09-24-1632523752-fdns_cname.json.gz sonar.json.gz
RUN python -m pip install requests

ENTRYPOINT ["python", "PyDNSRecon.py"]
