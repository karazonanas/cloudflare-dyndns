FROM python:3-alpine

WORKDIR /app

RUN apk update && \
    apk add --no-cache tzdata && \
    apk add --no-cache curl

ENV TZ=Europe/Berlin

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./
COPY logger.py ./

CMD [ "python", "./app.py" ]

HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost/healthz || exit 1


EXPOSE 80
