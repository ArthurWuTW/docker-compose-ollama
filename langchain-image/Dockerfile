FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y
RUN apt-get install -y iputils-ping init wget curl git sudo vim dumb-init
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get install -y python3.12
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.12 get-pip.py
RUN rm get-pip.py

RUN pip3.12 install langchain
RUN pip3.12 install flask --ignore-installed


COPY infinite-loop /infinite-loop

ENTRYPOINT ["/infinite-loop"]
