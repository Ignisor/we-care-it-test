FROM python:3.7-alpine

MAINTAINER Ignisor <german.g@gowombat.team>

RUN apk add --no-cache g++ make python3-dev jpeg-dev libffi-dev musl-dev

COPY . /app
WORKDIR /app
RUN apk --update add curl
HEALTHCHECK --interval=5s --timeout=3s --retries=3 \
      CMD curl -f http://localhost:80 || exit 1

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

RUN chmod +x docker-entrypoint.sh
