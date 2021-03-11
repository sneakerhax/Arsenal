FROM kalilinux/kali-rolling

RUN apt update && apt -y upgrade
RUN apt install -y metasploit-framework
COPY msfstart.sh .
RUN chmod +x msfstart.sh
ENTRYPOINT [ "bash", "./msfstart.sh" ]