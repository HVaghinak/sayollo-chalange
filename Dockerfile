FROM python:3.8

COPY . /app/
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "gunicorn", "-b", "0.0.0.0:80", "-c", "gunicorn.conf.py", "apps:create_app()" ]
