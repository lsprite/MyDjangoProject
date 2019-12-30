import json

from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

from MyDjangoProject import global_variable
from api.utils import dictfetchall, ComplexEncoder, ajax_res, check_email
from api.send_email import send_email


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


def testdb_post(request):
    cursor = connection.cursor()
    cursor.execute("select * from qyh_user limit %s", [2])
    rows = dictfetchall(cursor)
    json_str = json.dumps(rows, cls=ComplexEncoder)
    users_dict = json.loads(json_str)
    # return HttpResponse(json_str)
    return render(request, 'testdb_post.html', {'users': users_dict})
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
    return HttpResponse(message)


def search_post(request):
    request.encoding = 'utf-8'
    subject = request.POST['subject']
    msg = request.POST['msg']
    to_addr = request.POST['to_addr']
    if 'subject' not in request.POST or not subject:
        return return_error_HttpResponse(request, "", "主题不能为空")
    elif 'msg' not in request.POST or not msg:
        return return_error_HttpResponse(request, "", "内容不能为空")
    elif 'to_addr' not in request.POST or not to_addr:
        return return_error_HttpResponse(request, "", "接收人不能为空")
    elif 'to_addr' in request.POST and to_addr:
        if not check_email(to_addr):
            return return_error_HttpResponse(request, "", "请输入正确的邮箱格式")
    if send_email(to_addr, subject, msg):
        return return_succeed_HttpResponse(request, "", "发送成功")
    else:
        return return_error_HttpResponse(request, "", "发送失败")


def return_succeed_HttpResponse(request, value, message):
    return HttpResponse(ajax_res(global_variable.global_setting(request)['RES_CODE'], value, message),
                        content_type='application/json')


def return_error_HttpResponse(request, value, message):
    return HttpResponse(ajax_res(global_variable.global_setting(request)['ERROR_CODE'], value, message),
                        content_type='application/json')
