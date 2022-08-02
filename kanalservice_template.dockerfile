FROM ubuntu:latest

LABEL maintainer "Timur Ishankulov <timur@ishankulov.ru>"
RUN apt-get update && apt-get install -y \
nano git \
python3 python3-dev python3-pip python3.10-venv libmysqlclient-dev build-essential libpq-dev

WORKDIR "/srv"
RUN git clone https://github.com/TimurIshankulov/kanal-service.git/
WORKDIR "/srv/kanal-service"
RUN python3 -m pip install -r requirements.txt

RUN cp config_template.py config.py
RUN sed -i "s/user = 'user'/user = '<user>'/" config.py
RUN sed -i "s/password = 'password'/password = '<password>'/" config.py
RUN sed -i "s/database = 'database_name'/database = '<database_name>'/" config.py
RUN sed -i "s/host = 'localhost'/host = '<host>:<port>'/" config.py
COPY ./secret.json secret.json

ENTRYPOINT git pull --ff-only && python3 main.py