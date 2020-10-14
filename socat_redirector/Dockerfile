FROM kalilinux/kali-rolling
RUN apt update && apt upgrade -y
RUN apt install socat -y

ENTRYPOINT [ "socat", "TCP4-LISTEN:80,fork", "TCP4:<ip_address>:81" ]