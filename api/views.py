# Create your views here.
import json
import os
from django.db import connection
from django.http.response import HttpResponse

from api.utils import dictfetchall, ComplexEncoder, succeed, error
from django.views.defaults import page_not_found, server_error


def index(request):
    return HttpResponse(b'Hello World' + os.path)


def testdbApi(request):
    cursor = connection.cursor()
    cursor.execute("select * from qyh_user limit %s", [2])
    rows = dictfetchall(cursor)
    json_str = json.dumps(rows, cls=ComplexEncoder)
    users_dict = json.loads(json_str)
    # return HttpResponse(json_str)
    return HttpResponse(succeed(users_dict, "搜索成功"))


# def page_not_found(request, exception):
#     return HttpResponse(error("api不存在"))
# def page_error(request):
#     return HttpResponse(error("api错误"))


def my_page_not_found(request, exception):
    template_name = '404.html'
    if request.path.startswith('/api/'):
        template_name = 'api_error/404.html'
    return page_not_found(request, exception, template_name=template_name)


def my_page_error(request):
    template_name = '500.html'
    if request.path.startswith('/api/'):
        template_name = 'api_error/500.html'
    return server_error(request, template_name=template_name)
