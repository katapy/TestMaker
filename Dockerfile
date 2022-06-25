FROM python:alpine

WORKDIR /app

COPY ./app/ ./app/
COPY ./.env ./app/

RUN pip install --upgrade pip
RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python3 -m pip install -r app/requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

# test run
# RUN pytest -q app/test

CMD ["python", "app/main.py"]