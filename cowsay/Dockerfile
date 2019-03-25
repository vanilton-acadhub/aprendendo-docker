FROM debian:stretch
LABEL maintainer="github.com/vanilton-acadhub"

RUN apt-get update && apt-get install -y cowsay fortunes-br
COPY entrypoint.sh /

ENTRYPOINT [ "/entrypoint.sh" ]