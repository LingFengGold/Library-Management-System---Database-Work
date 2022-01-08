# 自定义中间类（执行是否登录判断）
from django.shortcuts import redirect
from django.urls import reverse
import re


class libraryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("libraryMiddleware")
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        path = request.path
        print("url:", path)

        # 判断管理后台是否登录
        # 后台不登录也能访问的url
        urllist = ['/myadmin/login', '/myadmin/logout', '/myadmin/dologin']
        # 判断当前请求url是否以/myadmin开头
        if re.match(r'/myadmin', path) and (path not in urllist):
            # 判断是否登录(session中没有adminuser)
            if 'adminuser' not in request.session:
                # 重定向到登录页
                return redirect(reverse("myadmin_login"))

        urllist2 = ['/login','/logout','/dologin','/doregister','/register']
        if not re.match(r'/myadmin', path) and (path not in urllist2):
            # 判断是否登录(session中没有user)
            if 'user' not in request.session:
                # 重定向到登录页
                return redirect(reverse("web_login"))

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
