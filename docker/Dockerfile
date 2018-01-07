FROM python:3

MAINTAINER marjara35@gmail.com

VOLUME ["/src"]

COPY main.py /src/main.py

RUN pip install ezrpy

WORKDIR /src

CMD ["python", "main.py"]

