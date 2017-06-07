# -*- coding:utf-8 -*- 


import json
import time

from flask import current_app


from extensions import celery
from extensions import db
from extensions import rd


@celery.task(name="cmdb.ci_cache", queue="cmdb_async")
def ci_cache(ci):
    time.sleep(0.1)
    db.session.close()
    ci_id = ci.ci_id
    rd.delete(ci_id)
    rd.add({ci_id: json.dumps(ci)})
    current_app.logger.info("%d caching.........." % ci_id)


@celery.task(name="cmdb.ci_delete", queue="cmdb_async")
def ci_delete(ci_id):
    current_app.logger.info(ci_id)
    rd.delete(ci_id)
    current_app.logger.info("%d delete.........." % ci_id)
