FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/src

ENTRYPOINT ["uvicorn", "src.main:app", "--workers", "6", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]