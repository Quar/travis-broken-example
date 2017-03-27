FROM ubuntu:16.04

# Update System
RUN apt-get update && \
    apt-get install --yes wget && \
    apt-get install --yes bzip2


# currently Docker will not expand variables in ENV, so we have to use hard code
# https://github.com/docker/docker/issues/2637
# https://github.com/docker/docker/issues/22595

# install conda
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p /root/miniconda && \
    rm miniconda.sh &&\
    /root/miniconda/bin/conda config --set always_yes True --set changeps1 no && \
    /root/miniconda/bin/conda info -a

COPY ./environment.yml $HOME/environment.yml

ENV PATH="/root/miniconda/bin:$PATH"

RUN /root/miniconda/bin/conda env create --name testenv --file environment.yml

ENV PATH="/root/miniconda/envs/testenv/bin:$PATH"

COPY . /$HOME/app

WORKDIR /$HOME/app

# in-place check for env setup
#RUN /bin/bash -c 'python3 -c "import pymysql"'