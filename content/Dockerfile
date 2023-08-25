FROM python:3.9

ADD . /app/content/

WORKDIR /app/content/

RUN pip install requests

CMD [ "python","content_test.py" ]