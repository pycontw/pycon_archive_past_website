FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

CMD ["python","-m","http.server","--cgi","8888"]



