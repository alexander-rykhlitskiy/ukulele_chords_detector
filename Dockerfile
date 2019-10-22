FROM jupyter/scipy-notebook:1386e2046833

WORKDIR /app
ADD requirements.txt ./
RUN pip install -r requirements.txt

CMD jupyter notebook
