FROM python:2.7-alpine
MAINTAINER Mario Inga <mario21ic@gmail.com>

# Dependencies 
COPY codedeploy.py /usr/bin/codedeploy
RUN chmod +x /usr/bin/codedeploy

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
