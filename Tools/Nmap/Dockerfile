FROM kalilinux/kali-rolling
RUN apt-get update && apt-get upgrade -y && apt-get -y install nmap
COPY add_nse_function .
RUN cat add_nse_function >> ~/.bashrc
ENTRYPOINT [ "nmap" ]
