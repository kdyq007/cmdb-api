# -*- coding:utf-8 -*-
__author__ = 'qiqi'

from __init__ import make_app
from extensions import celery

app = make_app('config.cfg')
app.app_context().push()

# 命令行执行以下命令：
# celery worker -A run_celery.celery -E -Q cmdb_web_async