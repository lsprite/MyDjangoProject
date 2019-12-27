# Create your views here.
import json

from django.db import connection
from django.http.response import HttpResponse

from api.utils import dictfetchall, ComplexEncoder, succeed


def index(request):
    return HttpResponse(b'Hello World')


def testdbApi(request):
    cursor = connection.cursor()
    cursor.execute("select * from qyh_user limit %s", [2])
    rows = dictfetchall(cursor)
    json_str = json.dumps(rows, cls=ComplexEncoder)
    users_dict = json.loads(json_str)
    # return HttpResponse(json_str)
    return HttpResponse(succeed(users_dict, "搜索成功"))
