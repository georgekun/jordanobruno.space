FROM python:3.10.12

RUN mkdir /app
WORKDIR /app

COPY ../../backend/ /app/

COPY ../../docker/ /app/docker/
RUN pip install --no-cache-dir -r requirements.txt
  

RUN chmod +x /app/docker/backend/entrypoint.sh
