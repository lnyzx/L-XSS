#!/usr/bin/env python
# # -*- coding: utf-8 -*-

import time, json, re, base64
from .io_funcs import *


# 整理需要记录的信息，同时存储文件
def get_data_from_req(request):
    data = {}
    data['req_ip'] = get_real_ip(request)
    if 'SERVER_PORT' in request.META:
        data['req_port'] = request.META['SERVER_PORT']
    data['req_method'] = request.method
    data['req_ip_addr'] = get_ip_addr(data['req_ip'])
    data['req_header'] = get_header_from_req(request)
    data['req_path'] = request.path
    data['req_time'] = int(time.time())
    data['get_data'] = request.GET
    data['post_data'] = request.POST
    data['cookie_data'] = request.COOKIES
    json_data = json.dumps(data)
    save_data_to_file(json_data, data['req_time'])
    return json_data


# 获取请求中的headers，返回字典
def get_header_from_req(request):
    m = re.compile("^HTTP_")
    request_method = request.method
    request_headers = request.META.items()
    all_header = {}
    for k, v in request_headers:
        if m.match(k):
            k = k[5:].title()
            all_header[k] = v
        else:
            pass
    return all_header


# 获取真实ip，返回字符串
def get_real_ip(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    return ip


# 获取ip地址的物理地址，默认为未知，返回字符串
def get_ip_addr(ip):
    ip_addr = "未知"
    return ip_addr


# 从文件中得到所有的记录数据
def load_all_data():
    data = []
    file_names = get_data_file_name()
    for each_file in file_names:
        this_data = load_data_from_file(each_file)
        data.append(this_data)
    return data