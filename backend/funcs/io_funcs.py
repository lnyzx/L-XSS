#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64, glob, os, re
from django.conf import settings

DATA_FOLDER = settings.DATA_ROOT
PROBE_FOLDER = settings.PROBE_ROOT
TEMPLATES_FOLDER = settings.TEMPLATES_ROOT


def base64_encode(data):
    return base64.b64encode(data)


# 存储请求的headers，参数，存储至data目录下，用时间戳命名每一个请求
def save_data_to_file(json_data, this_time):
    data = data_encrypt(json_data)
    file_name = DATA_FOLDER + str(this_time) + '.log'
    with open(file_name, 'w') as f:
        f.write(data)
    return 0

# 读取存储在文件中的所有data，输出json
def load_data_from_file(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
        data = data_decrypt(data)
    return data


# 遍历data目录，得到所有log文件名
def get_data_file_name():
    file_names = glob.glob(DATA_FOLDER + '*.log')
    return file_names


# 加密函数
def data_encrypt(data):
    return data


# 解密函数
def data_decrypt(data):
    return data


# 删除data，分为根据时间戳删除和全部删除
def delete_data(request):
    if request.POST.get('id', '0') == "all":
        all_file = get_data_file_name()
        for i in all_file:
            os.remove(i)
        return "0"
    else:
        id = request.POST.get('id', '0')
        if id.isdigit():
            try:
                os.remove(DATA_FOLDER + id + '.log')
            except Exception as e:
                pass


# 从dist文件夹中取得所有probe的名字
def get_all_probes():
    file_names = [name for name in os.listdir(PROBE_FOLDER) if name.endswith('.js')]
    return file_names


# 写入probe
def wirte_probe2file(name, content):
    content = base64.b64decode(content).decode('utf-8')
    probe_file_name = os.path.join(PROBE_FOLDER, name + '.js')
    with open(probe_file_name, 'w') as f:
        f.write(content)
    return "1"


# 删除probe
def delete_probe(request):
    # pass
    if request.POST.get('name', '0') == "all":
        for probes in glob.glob(PROBE_FOLDER + '*.js'):
            os.remove(probes)
        return "1"
    else:
        name = request.POST.get('name', '0')
        if (delete_waf(name) == 0):
            probe_file_name = os.path.join(PROBE_FOLDER, name)
            try:
                os.remove(probe_file_name)
            except Exception as e:
                pass
        return "1"


# 获取所有templates文件名
def get_all_templates():
    file_names = [name for name in os.listdir(TEMPLATES_FOLDER)]
    return file_names


# 防止任意文件删除
def delete_waf(strr):
    if strr.endswith('.js'):
        if re.search('[^a-zA-Z0-9_-]', strr.split('.js')[0]):
            return 1
        else:
            return 0
     else:
        return 1