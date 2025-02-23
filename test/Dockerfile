FROM python:3.13.2-bookworm

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY script.py .

EXPOSE 8000

ENTRYPOINT ["python", "script.py"]
