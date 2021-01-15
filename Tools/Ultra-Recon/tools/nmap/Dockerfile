FROM kalilinux/kali-rolling
RUN apt-get update && apt-get upgrade -y
RUN apt-get update && apt-get -y install nmap
ENTRYPOINT [ "nmap" ]