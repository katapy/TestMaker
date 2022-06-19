FROM python:alpine

WORKDIR /app

COPY ./app/ ./app/

RUN pip install -r app/requirements.txt

CMD ["python", "app/main.py"]