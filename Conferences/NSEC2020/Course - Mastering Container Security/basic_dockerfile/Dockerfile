FROM alpine:latest

RUN apk update && apk add nikto && rm -rf /var/cache/apk/*

CMD ["nikto.pl"]
