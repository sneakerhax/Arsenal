FROM kalilinux/kali-rolling

RUN apt-get update && apt-get upgrade -y
RUN apt-get install whatweb -y

ENTRYPOINT [ "whatweb" ]