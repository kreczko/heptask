#! /usr/bin/env bash

DAEMONS="\
    mysqld \
    cloudera-quickstart-init \
    zookeeper-server \
    hadoop-hdfs-datanode \
    hadoop-hdfs-journalnode \
    hadoop-hdfs-namenode \
    hadoop-hdfs-secondarynamenode"

for daemon in ${DAEMONS}; do
    sudo service ${daemon} start
done

# prevent container from exiting after services are started
tail -f /dev/null
