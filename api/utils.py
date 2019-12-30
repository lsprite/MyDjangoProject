import decimal
import json
import re
from datetime import date, datetime


def succeed(rows, msg):
    return json.dumps({'code': '10000', 'value': rows, 'message': msg})


def error(msg):
    return json.dumps({'code': '-1', 'value': "", 'message': msg})


def ajax_res(code, value, msg):
    return json.dumps({'code': code, 'value': value, 'message': msg})


def dictfetchall(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()]


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            return json.JSONEncoder.default(self, obj)


def check_email(addr):
    if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', addr):
        # if re.match(r'[0-9a-zA-Z_]{0,19}@163.com',text):
        return True
    else:
        return False
