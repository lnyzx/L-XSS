from django.test import TestCase
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render

from backend.funcs.data_funcs import *
from backend.funcs.user_funcs import *
import time, json, re, base64, requests
from functools import reduce
from urllib import request
from backend.funcs.io_funcs import *
