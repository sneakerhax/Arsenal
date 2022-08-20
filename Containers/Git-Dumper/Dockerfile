# A dockerized version of the tool git-dumper by arthaud

FROM python:3

RUN apt update && apt upgrade -y && apt install -y git
RUN git clone https://github.com/arthaud/git-dumper
WORKDIR /git-dumper
RUN pip3 install -r requirements.txt


ENTRYPOINT ["python", "git_dumper.py"]