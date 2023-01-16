FROM python:3.10-alpine

WORKDIR /app

COPY redirect.py ./
COPY 404.html /
COPY style.css /
COPY url-lists ./url-lists

RUN pip install flask

EXPOSE 80
ENTRYPOINT [ "python", "./redirect.py" ]
