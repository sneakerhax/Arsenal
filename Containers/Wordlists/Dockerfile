FROM alpine

RUN apk -U upgrade && apk add git wget
COPY download_wordlists.sh download_wordlists.sh
RUN chmod +x download_wordlists.sh && mkdir wordlists
WORKDIR /wordlists

ENTRYPOINT [ "sh", "/download_wordlists.sh" ]
