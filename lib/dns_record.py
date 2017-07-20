#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'qiqi'
from flask import current_app
from extensions import db
from models.dns_record import DnsRecord
from models import row2dict


class DnsRecordManager(object):
    def search_records(self, args, page=1, count=None):
        if count is None:
            count = current_app.config.get("DEFAULT_PAGE_COUNT")
        records = db.session.query(DnsRecord)
        if args.get("isp"):
            records = records.filter(
                DnsRecord.isp.ilike("%{0}%".format(args.get("isp"))))
        if args.get("record_type"):
            records = records.filter(
                DnsRecord.record_type == args.get("record_type"))
        if args.get("record"):
            records = records.filter(
                DnsRecord.record.ilike("%{0}%".format(args.get("record"))))
        if args.get("record_value"):
            records = records.filter(DnsRecord.record_value.ilike(
                "%{0}%".format(args.get("record_value"))))
        if args.get("comment"):
            records = records.filter(
                DnsRecord.comment.ilike("%{0}%".format(args.get("comment"))))
        numfound = records.count()
        records = records.offset((page - 1) * count).limit(count).all()
        res = list()
        for record in records:
            res.append(row2dict(record))
        return numfound, page, res
