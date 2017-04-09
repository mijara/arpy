FROM python:2

MAINTAINER marjara35@gmail.com

VOLUME ["/src"]

RUN pip install cython
RUN pip install ezrpy

WORKDIR /src

CMD ["python", "main.py"]

