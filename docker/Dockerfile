FROM ubuntu:16.04

RUN apt update && apt upgrade -y

#htcondor needs keyboard configuration
RUN apt install -y debconf-utils apt-utils keyboard-configuration sudo && \
    apt clean
COPY keylayout.conf /tmp/keylayout.conf
RUN debconf-set-selections < /tmp/keylayout.conf && \
    dpkg-reconfigure keyboard-configuration -f noninteractive

RUN apt install -y condor python-pip && apt clean
RUN pip install --upgrade pip && pip install htcondor

RUN useradd -ms /bin/bash testuser && \
    echo "testuser:testuser" | chpasswd && \
    adduser testuser sudo && \
    echo "user ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/user


RUN pip install  supervisor supervisor-stdout
COPY 	supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY 99_custom.conf /etc/condor/config.d/99_custom.conf

WORKDIR /home/testuser
COPY run.sh /tmp/run.sh

CMD ["/tmp/run.sh"]
