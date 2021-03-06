FROM python:3.4.3


RUN apt-get -y update

RUN apt-get -y upgrade

RUN apt-get install lrzsz

RUN apt-get install nano

RUN apt-get install unzip

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install -r requirements.txt

RUN wget https://github.com/evernote/evernote-sdk-python3/archive/master.zip;unzip master.zip;cd evernote-sdk-python3-master;python setup.py install

CMD uwsgi --ini /usr/src/app/webapp2/webapp2/wsgi.ini

EXPOSE 8000