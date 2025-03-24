FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y
RUN apt-get install -y iputils-ping init wget curl git sudo vim dumb-init

COPY infinite-loop /infinite-loop

ENTRYPOINT ["/infinite-loop"]
