#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from urllib.parse import urlparse
from django.conf import settings
import hashlib


def md5(strr):
    return hashlib.md5(strr.encode('utf-8')).hexdigest()


# 判断是否登录
def is_login(request):
    if request.session.get('is_login', 0) == 1:
        return True
    else:
        return False


# 登录函数
def check_login(request):
    pass_nonce = request.session['pass_nonce']
    enc_passwd = md5(settings.MD5_PASSWD + pass_nonce)
    passwd = request.POST.get("passwd", "0")
    if passwd == enc_passwd:
        request.session['is_login'] = 1
        return 1
    else:
        return 0


# 注销
def logout(request):
    request.session['is_login'] = 0


# 判断referer是否与settings中设置的base_url同源
def check_referer(request):
    if 'HTTP_REFERER' not in request.META:
        return False
    this_host = settings.BASE_URI
    req_referer = request.META.get('HTTP_REFERER')
    req_referer_host = urlparse(req_referer).hostname
    req_referer_port = urlparse(req_referer).port
    if req_referer_port:
        req_referer = req_referer_host + ":" + str(req_referer_port)
    else:
        req_referer = req_referer_host
    if this_host == req_referer:
        return True
    else:
        return False