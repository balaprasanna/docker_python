FROM python:3.7

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY app.py app.py

EXPOSE 8022

CMD ["python", "app.py"]
