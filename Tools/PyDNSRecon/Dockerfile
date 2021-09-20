FROM python:3

RUN apt update && apt upgrade -y
RUN mkdir PyDNSRecon
COPY PyDNSRecon.py /PyDNSRecon
WORKDIR /PyDNSRecon
RUN wget https://github.com/OWASP/Amass/releases/download/v3.13.4/amass_linux_amd64.zip && unzip amass_linux_amd64.zip && mv amass_linux_amd64 amass
RUN wget https://opendata.rapid7.com/sonar.fdns_v2/2021-08-27-1630022740-fdns_cname.json.gz && mv 2021-08-27-1630022740-fdns_cname.json.gz sonar.json.gz
RUN pip install requests

ENTRYPOINT ["python", "PyDNSRecon.py"]
