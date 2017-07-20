#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'qiqi'

from flask import Blueprint, request, jsonify

from lib.utils import get_page
from lib.utils import get_per_page
from lib.dns_record import DnsRecordManager

dnsrecord = Blueprint("dnsrecord", __name__)

@dnsrecord.route("", methods=["GET"])
def search_records():
    page = get_page(request.values.get("page", 1))
    count = get_per_page(request.values.get("count"))

    isp = request.values.get("isp", "")
    record_type = request.args.get("record_type", "")
    record = request.args.get("record", "")
    record_value = request.args.get("record_value", "")
    comment = request.args.get("comment", "")

    args = {
        "isp": isp,
        "record_type": record_type,
        "record": record,
        "record_value": record_value,
        "comment": comment,
    }
    manager = DnsRecordManager()
    numfound, page, res = manager.search_records(args, page, count)
    return jsonify(numfound=numfound, page=page, records=res)
