FROM python:3.9

COPY . .

RUN pip install --upgrade pip

RUN pip install dataclasses

RUN pip install aiogram

RUN pip install environs

RUN pip install aio_pika

CMD ["python","bot.py"]