FROM python:3.7-alpine

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY . ./

WORKDIR /app

CMD [ "python", "-u", "app.py" ]
