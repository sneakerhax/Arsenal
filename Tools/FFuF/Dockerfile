FROM golang:alpine

RUN apk -U upgrade
RUN go install github.com/ffuf/ffuf@latest

ENTRYPOINT [ "ffuf" ]