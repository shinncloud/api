FROM python:3.7.3
RUN pip install pip-tools
COPY . /usr/src/app
RUN pip-sync /usr/src/app/requirements.txt
EXPOSE 5000
WORKDIR /usr/src/app
CMD gunicorn -w 4 -b 0.0.0.0:5000 --error-logfile - --access-logfile - echoer:app
