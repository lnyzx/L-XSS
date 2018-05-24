from .funcs.user_funcs import is_login, check_referer
from django.http import HttpResponseRedirect

# 判断referer是否是同源，不是则丢弃请求，防止CSRF
class RefererMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.path == '/':
            response = self.get_response(request)
        elif request.method == 'GET':
            response = self.get_response(request)
        elif request.method == 'POST' and check_referer(request):
            response = self.get_response(request)
        else:
            response = HttpResponseRedirect('/auth/')

        # Code to be executed for each request/response after
        # the view is called.

        return response

