#!/usr/bin/bash
# @author by wangcw
# @generate at 2023/9/20 15:39

ps aux | grep "gunicorn" | grep -v grep | awk '{print $2}' | xargs kill -9

gunicorn app.main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker -b 0.0.0.0:5001