import json

from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from api.utils import dictfetchall, ComplexEncoder


def testdb(request):
    cursor = connection.cursor()
    cursor.execute("select * from qyh_user limit %s", [2])
    rows = dictfetchall(cursor)
    json_str = json.dumps(rows, cls=ComplexEncoder)
    users_dict = json.loads(json_str)
    # return HttpResponse(json_str)
    return render(request, 'testdb.html', {'users': users_dict})
    # return HttpResponse(json.dumps(rows))
    # return JsonResponse(rows, safe=False, json_dumps_params={'ensure_ascii': False})
    # return JsonResponse(succeed(rows, "1212"), safe=False, json_dumps_params={'ensure_ascii': False})
    # return HttpResponse(succeed(rows, "1212"))


def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse("收到")
