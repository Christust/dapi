FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /home/app

RUN pip install --upgrade pip

COPY . ./

RUN pip install -r requirements.txt

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000