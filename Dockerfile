FROM python:3.6-alpine

WORKDIR /app

ADD requirements.txt /app

RUN cd /app && \
    pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "./lib/blockchain.py", "--port", "5000"]
