#!/usr/bin/env python
# # -*- coding: utf-8 -*-

import time, json, re, base64, datetime, pytz
from functools import reduce
from urllib import request
from .io_funcs import *

tz = pytz.timezone('Asia/Shanghai')

# 处理请求中的参数，返回json
def parse_cmd(request):
    cmd_list = {
        'listallid': list_all_id(request),
        'list': list_by_page(request),
        'delete': delete_data(request),
        0: 0,
    }
    return cmd_list.get(request.GET.get('cmd', 0))

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
    data['req_formattime'] = datetime.datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
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
    if check_local_ip(ip):
        return '局域网'
    try:
        apiurl = "http://www.ip138.com/ips138.asp?ip=%s&action=1" % ip
        content = request.urlopen(apiurl).read().decode("GBK")
        match_compile = re.compile(r'<td align="center"><ul class="ul1"><li>.*?</li>')
        ip_addr = re.findall(match_compile, content)[0][44:-5]
    except Exception as e:
        ip_addr = "未知"
    return ip_addr


# 判断ip是否是局域网
def ip_into_int(ip):
    return reduce(lambda x,y:(x<<8)+y,map(int,ip.split('.')))

def check_local_ip(ip):
    ip = ip_into_int(ip)
    net_a = ip_into_int('10.255.255.255') >> 24
    net_b = ip_into_int('172.31.255.255') >> 20
    net_c = ip_into_int('192.168.255.255') >> 16
    return ip >> 24 == net_a or ip >>20 == net_b or ip >> 16 == net_c


# 从文件中得到所有的记录数据
def load_all_data():
    data = []
    file_names = get_data_file_name()
    for each_file in file_names:
        this_data = load_data_from_file(each_file)
        data.append(this_data)
    return json.dumps(data)

# 获取所有记录的id(即时间戳)
def list_all_id(request):
    data = []
    file_names = get_data_file_name()
    for each_file in file_names:
        this_data = json.loads(load_data_from_file(each_file))
        this_data_id = this_data['req_time']
        this_data_ip = this_data['req_ip']
        this_data_addr = this_data['req_ip_addr']
        outdata = {}
        outdata['id'] = this_data_id
        outdata['ip'] = this_data_ip
        outdata['addr'] = this_data_addr
        data.append(outdata)
    return json.dumps(data)


# 根据页码和每页数量得到记录
def list_by_page(request):
    page = int(request.POST.get('page', '1'));
    page_num = int(request.POST.get('page_number', '25'));
    data = []
    file_names = get_data_file_name()
    for each_file in file_names:
        this_data = load_data_from_file(each_file)
        data.append(this_data)
    data_sort(data)
    return json.dumps(data[((page - 1) * page_num): (((page - 1) * page_num) + page_num)])
    # return json.dumps(data)

# 排序data，由于不同操作系统读取文件的顺序不同，所以要按照时间戳进行排序
def data_sort(data):
    for passnum in range(0, len(data) - 1, 1):  
        for i in range(0, len(data) - passnum - 1, 1):  
            if (get_reqtime(data[i]) < get_reqtime(data[i+1])):  
                tmp = data[i+1]  
                data[i+1] = data[i]  
                data[i] = tmp 


def get_reqtime(data):
    tmp = json.loads(data)
    return tmp['req_time']