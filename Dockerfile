FROM ubuntu:16.04

# Update System
RUN apt-get update && \
    apt-get install --yes wget && \
    apt-get install --yes bzip2

# install conda
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p $HOME/miniconda && \
    rm /miniconda.sh && \
    conda config --set always_yes True --set changeps1 no && \
    conda info -a

ENV PATH "$HOME/miniconda/bin:$PATH"

# Config conda Environment, note it would be easy to update to root env
COPY ./environment.yml $HOME/environment.yml
#RUN /root/miniconda/bin/conda env create --name test_env --file /root/environment.yml
#RUN /root/miniconda/bin/conda-env update --name root --file /root/environment.yml

COPY ./ /$HOME/

#RUN /bin/bash -c 'python3 /root/test/package_test.py'
#RUN /bin/bash -c 'python3 /root/test/package_test.py'