FROM centos:6

RUN adduser condor

RUN curl -o /etc/yum.repos.d/htcondor-stable-rhel6.repo http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-rhel6.repo

RUN yum install -y condor
