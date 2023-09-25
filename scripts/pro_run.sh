#!/usr/bin/bash
# @author by wangcw
# @generate at 2023/9/20 15:39

# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
ps aux | grep "gunicorn" | grep -v grep | awk '{print $2}' | xargs kill -9

gunicorn app.main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker -b 0.0.0.0:5001 --keyfile app/config/key.pem --certfile app/config/cert.pem
