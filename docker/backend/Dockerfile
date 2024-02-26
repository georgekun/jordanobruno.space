FROM python:3.10.12

RUN mkdir /app
WORKDIR /app

COPY ../../backend/ /app/

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
  

RUN chmod +x /app/server-entrypoint.sh
