FROM python:3.10.2-alpine3.15

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

ENTRYPOINT [ "python", "main.py" ]