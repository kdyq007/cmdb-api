# -*- coding:utf-8 -*- 

from extensions import db


class DnsRecord(db.Model):
    __tablename__ = "dns_record"

    isp = db.Column(db.CHAR(8), nullable=False, primary_key=True)
    record = db.Column(db.CHAR(8), nullable=False, primary_key=True)
    record_type = db.Column(db.CHAR(8))
    record_value = db.Column(db.CHAR(8), nullable=False, primary_key=True)
    comment = db.Column(db.CHAR(8))
