FROM python:3.8.6-alpine3.12

# 타임존 설정
RUN apk add tzdata && \
    cp /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \
    echo "Asia/Seoul" > /etc/timezone

RUN apk add --no-cache --virtual .build-deps gcc musl-dev python3-dev

ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p /src
ADD . /src

#CMD ["celery", "-A", "src", "worker", "--loglevel=info"]

CMD ["celery", "-A", "src:app", "worker", "-l", "info"]





