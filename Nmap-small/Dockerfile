FROM alpine:3.15

RUN apk -U upgrade
RUN apk add nmap
RUN apk add nmap-scripts

ENTRYPOINT ["nmap"]