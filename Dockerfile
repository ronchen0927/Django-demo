FROM python:3
ENV PYTHONUNBUFFERD 1
RUN mkdir /django-files
WORKDIR /django-files
RUN git clone https://github.com/ronchen0927/Django-demo.git
RUN pip install Django
RUN pip install mysqlclient
ENTRYPOINT python Django-demo/djangosite/manage.py runserver 0.0.0.0:80
