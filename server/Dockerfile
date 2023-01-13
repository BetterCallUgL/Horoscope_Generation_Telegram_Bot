FROM continuumio/miniconda3

COPY . .

RUN conda install python=3.8 pytorch cudatoolkit -c pytorch

RUN pip install aio_pika

RUN pip install transformers

CMD ["python","server.py"]