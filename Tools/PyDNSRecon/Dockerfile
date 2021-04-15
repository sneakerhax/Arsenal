FROM python:3

RUN mkdir PyDNSRecon
COPY PyDNSRecon.py /PyDNSRecon
WORKDIR /PyDNSRecon
RUN wget https://github.com/OWASP/Amass/releases/download/v3.11.13/amass_linux_amd64.zip && unzip amass_linux_amd64.zip && mv amass_linux_amd64 amass
RUN wget https://opendata.rapid7.com/sonar.fdns_v2/2021-03-26-1616717552-fdns_cname.json.gz && mv 2021-03-26-1616717552-fdns_cname.json.gz sonar.json.gz
RUN pip install requests

ENTRYPOINT ["python", "PyDNSRecon.py"]
