# -*- coding: utf-8 -*-


from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache
from celery import Celery
from lib.utils import RedisHandler


__all__ = ['mail', 'db', 'cache', 'celery', "rd"]


mail = Mail()
db = SQLAlchemy()
cache = Cache()
celery = Celery()
rd = RedisHandler()
