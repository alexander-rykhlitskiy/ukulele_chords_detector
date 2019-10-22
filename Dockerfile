FROM jupyter/scipy-notebook:1386e2046833

RUN pip install tensorflow==2.0.0
RUN pip install jupytext==1.2.4

WORKDIR /app

CMD jupyter notebook
