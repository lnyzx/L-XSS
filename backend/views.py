from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render

from backend.funcs.data_funcs import *
from backend.funcs.user_funcs import *


def index(request):
    data = get_data_from_req(request)
    return HttpResponse(data)


# 记录的数据接口
def data(request):
    data = load_all_data()
    if is_login(request):
        return HttpResponse(data)
    else:
        return HttpResponseRedirect('/auth/')


# 用户登录管理接口
def auth(request):
    if request.method == 'POST' and request.POST.get('logout', '0') != '1':
        check_login(request)
    elif request.POST.get('logout', '0') == '1':
        logout(request)

    if is_login(request):
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')