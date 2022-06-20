FROM python:3.9.13-alpine3.16
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py migrate
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
CMD python manage.py runserver 0.0.0.0:80
