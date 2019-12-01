FROM ubuntu:bionic
RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN apt-get install python-pip -y
RUN pip --version; pip install --upgrade pip
RUN mkdir /opt/ethplorer_io/
COPY ./ /opt/ethplorer_io/
RUN pip install /opt/ethplorer_io/.
