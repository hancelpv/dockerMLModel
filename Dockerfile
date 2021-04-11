FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY train.py predict.py main.py ./

ADD data ./data

RUN echo $(ls -lh ./)

CMD [ "python", "./main.py" ]