FROM python:3.10-slim

WORKDIR /app

COPY interview.py /app/interview.py

COPY requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "/app/interview.py"]