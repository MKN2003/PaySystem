FROM python:latest

COPY . /paymentsystem

WORKDIR /paymentsystem

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver",]