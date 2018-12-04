FROM python:3-slim

RUN apt-get -y clean && \
    apt-get -y update && \
    apt-get -y install python3-dev && \
    apt-get -y install build-essential

ENV APP /usr/src/app

WORKDIR $APP

EXPOSE 5000

COPY . .

RUN pip install -r requirements.txt

CMD ["uwsgi", "--ini", "uwsgi.ini"]
