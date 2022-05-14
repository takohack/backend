#! /bin/bash
sudo redis-server /etc/redis/redis.conf
python3 manage.py runserver 0.0.0.0:8000