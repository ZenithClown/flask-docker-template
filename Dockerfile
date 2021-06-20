# ==========================================
#   Copyright (c) 2020 Debmalya Pramanik   #
# ==========================================

# -------------------------------------------------------------------
#   Mnemonic:   Dockerfile
#   Abstract:   Hello-World Flask REST-API Docker Template
#
#   Date:       15 April 2021
#   Author:     Debmalya Pramanik
# -------------------------------------------------------------------

FROM tiangolo/uwsgi-nginx-flask:python3.8
MAINTAINER Debmalya Pramanik <dPramanik.official@gmail.com>

ENV INSTALL_PATH /usr/src/helloworld
RUN mkdir -p $INSTALL_PATH

# install net-tools
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    net-tools \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# set working directory
WORKDIR $INSTALL_PATH

# setup flask environment
# install all requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy all files and folder to docker
COPY . .

# run the application in docker environment
CMD [ "python", "./manage.py" ]
