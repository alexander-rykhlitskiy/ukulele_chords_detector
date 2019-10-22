FROM jupyter/scipy-notebook:1386e2046833

RUN pip install tensorflow==2.0.0

WORKDIR /app

CMD jupyter notebook
