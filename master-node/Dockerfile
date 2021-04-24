FROM python:3.6-alpine

WORKDIR /app

COPY requirements.txt /app

RUN cd /app && \
    pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run"]
