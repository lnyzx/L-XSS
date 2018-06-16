#!/usr/bin/env python
# # -*- coding: utf-8 -*-
import base64, json
from .io_funcs import *


# 处理probe的请求
def parse_cmd_probe(request):
	cmd = request.GET.get('cmd', 0)
	if (cmd == 'getallprobe'):
		return list_all_probe(request)
	elif (cmd == 'createprobe'):
		return create_probe(request)
	elif (cmd == 'deleteprobe'):
		return delete_probe(request)
	elif (cmd == 'getalltemplates'):
		return list_all_templates(request)
	else:
		return '0'


# 获取所有probe的名字
def list_all_probe(request):
	probe_names = get_all_probes()
	data = probe_names
	return json.dumps(data)


# 根据code创建probe
def create_probe(request):
	content = request.POST.get('content', 'YWxlcnQoL2xueWFzLyk7')
	name = request.POST.get('name', 'x.js')
	return wirte_probe2file(name, content)


# 获得所有templates的名字
def list_all_templates(request):
	templates = get_all_templates()
	return json.dumps(templates)