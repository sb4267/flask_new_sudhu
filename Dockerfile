FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip



RUN mkdir /new_app

WORKDIR /new_app

ADD . /new_app/

RUN apk update
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

CMD python application.py
