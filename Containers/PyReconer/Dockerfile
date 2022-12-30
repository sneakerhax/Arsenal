FROM --platform=linux/x86_64 python:alpine

RUN apk -U upgrade && apk add bash wget nmap unzip git
RUN mkdir PyReconer
COPY PyReconer.py /PyReconer
WORKDIR /PyReconer
RUN mkdir output
RUN wget https://github.com/OWASP/Amass/releases/download/v3.14.2/amass_linux_amd64.zip && unzip amass_linux_amd64.zip && mv amass_linux_amd64 amass
RUN git clone https://github.com/FortyNorthSecurity/EyeWitness.git && ./EyeWitness/Python/setup/setup.sh
RUN python3 -m pip install netaddr selenium

ENTRYPOINT ["python3", "PyReconer.py"]

