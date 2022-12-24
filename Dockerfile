FROM python:latest
RUN pip install aiogram
RUN pip install python-dotenv

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


COPY . /usr/src/app


CMD ["python3", "./app.py"]
