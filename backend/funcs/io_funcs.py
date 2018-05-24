#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64, glob
from django.conf import settings

DATA_FOLDER = settings.DATA_ROOT


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