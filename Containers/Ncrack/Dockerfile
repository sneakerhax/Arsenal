FROM kalilinux/kali-rolling
RUN apt-get update && apt-get upgrade -y && apt-get -y install nmap ncrack
COPY add_nse_function .
RUN cat add_nse_function >> ~/.bashrc
ENTRYPOINT [ "ncrack" ]