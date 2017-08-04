FROM ubuntu:16.04

RUN apt update && apt upgrade -y

ARG DOCKER_FILES=docker
ARG TEST_USER=testuser

#htcondor needs keyboard configuration
RUN apt update && apt install -y \
  debconf-utils \
  apt-utils \
  keyboard-configuration \
  sudo \
  inetutils-ping \
  && apt clean
COPY ${DOCKER_FILES}/keylayout.conf /tmp/keylayout.conf
RUN debconf-set-selections < /tmp/keylayout.conf && \
    dpkg-reconfigure keyboard-configuration -f noninteractive

RUN apt install -y \
  condor \
  python-pip \
  git \
  wget \
  && apt clean
RUN pip install --upgrade pip && pip install htcondor

RUN useradd -ms /bin/bash ${TEST_USER} && \
    echo "${TEST_USER}:${TEST_USER}" | chpasswd && \
    adduser ${TEST_USER} sudo && \
    echo "${TEST_USER} ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/${TEST_USER}


RUN pip install supervisor supervisor-stdout
COPY ${DOCKER_FILES}/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ${DOCKER_FILES}/99_custom.conf /etc/condor/config.d/99_custom.conf

WORKDIR /home/testuser
COPY ${DOCKER_FILES}/start.sh /tmp/start.sh
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

USER ${TEST_USER}

CMD ["sudo", "/tmp/start.sh"]
