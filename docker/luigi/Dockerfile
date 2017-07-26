FROM python:alpine

ARG DOCKER_FILES=docker
ARG user=luigi
ARG group=luigi
ARG uid=1337
ARG gid=1337

RUN addgroup -g ${gid} ${group} \
    && adduser -u ${uid} -G ${group} -D -s /bin/bash ${user}

RUN pip install sqlalchemy luigi

RUN mkdir /etc/luigi
ADD ${DOCKER_FILES}/etc/luigi/logging.cfg /etc/luigi/
ADD ${DOCKER_FILES}/etc/luigi/client.cfg /etc/luigi/

RUN mkdir -p /luigi/logs
RUN mkdir -p /luigi/state

RUN chown -R ${user}:${group} /luigi
VOLUME /luigi/logs
VOLUME /luigi/state

EXPOSE 8082

USER ${user}

ENTRYPOINT ["luigid"]
