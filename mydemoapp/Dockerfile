FROM windows:latest

WORKDIR /app

RUN apt-get update
RUN apt-get install -y python-pip

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./app
EXPOSE 8000
CMD python /app/manage.py runserver 0.0.0.0:8000
