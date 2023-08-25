FROM python:3.9

ADD . /app/authorization/

WORKDIR /app/authorization/

RUN pip install requests

CMD [ "python","authorization_test.py" ]