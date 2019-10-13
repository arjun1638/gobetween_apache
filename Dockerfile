ARG BASE_IMAGE=ubuntu:xenial

# ---------------------  dev (build) image --------------------- #

FROM golang:1.12-alpine as builder

RUN apk add git
RUN apk add make

RUN mkdir -p /opt/gobetween
WORKDIR /opt/gobetween

RUN mkdir ./src
COPY ./src/go.mod ./src/go.mod
COPY ./src/go.sum ./src/go.sum

COPY go.mod .
COPY go.sum .

RUN go mod download

COPY . .

RUN make build-static

# --------------------- final image --------------------- #

FROM $BASE_IMAGE

WORKDIR /

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=builder /opt/gobetween/bin/gobetween  .
#ADD gobetween.toml /etc/gobetween/conf/gobetween.toml
ADD /t1/gobetween.toml /etc/gobetween/conf/
#CMD ["/gobetween", "-c", "/etc/gobetween/conf/gobetween.toml"]
RUN mkdir /tngbench_share

ADD start.sh start.sh
RUN chmod +x start.sh
ADD stop.sh stop.sh
RUN chmod +x stop.sh

CMD /bin/bash
