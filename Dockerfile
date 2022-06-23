FROM python:alpine

WORKDIR /app

COPY ./app/ ./app/
COPY ./.env ./app/

RUN pip install -r app/requirements.txt
RUN pytest -q app/test

CMD ["python", "app/main.py"]