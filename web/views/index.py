# Create your views here.
from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse

from myadmin.models import Member


# 后台管理首页
def index(request):
    return render(request, 'web/index/index.html')


# 会员登录表单
def login(request):
    return render(request, 'web/index/login.html')


# 会员注册表单
def register(request):
    return render(request, 'web/index/register.html')


# 执行管理员登录
def dologin(request):
    try:
        # 根据登录账号获取登录者信息
        user = Member.objects.get(username=request.POST['username'])
        # 判断当前用户是否是管理员
        if user.status == 1 or user.status == 6:
            # 判断登录密码是否相同
            import hashlib
            md5 = hashlib.md5()
            s = request.POST['pass'] + user.password_salt  # 从表单中获取密码并添加干扰值
            md5.update(s.encode('utf-8'))  # 将要产生md5的子串放进去
            if user.password_hash == md5.hexdigest():  # 获取md5值
                print('登录成功')
                # 将当前登录成功的用户信息以adminuser为key写入到session中
                if user.status == 1:
                    request.session['user'] = user.toDict()
                else:
                    request.session['adminuser'] = user.toDict()
                # 重定向到后台管理首页
                return redirect(reverse("web_index"))
            else:
                context = {"info": "登录密码错误！"}
        else:
            context = {"info": "无效的登录账号！"}
    except Exception as err:
        print(err)
        context = {"info": "登录账号不存在!"}
    return render(request, "web/index/login.html", context)


# 执行管理员注册
def doregister(request):
    try:
        terms = request.POST['terms']
        if terms == 'agree':
            ob = Member()
            username = request.POST['username']
            if Member.objects.filter(username=username).count() > 0:
                context = {'info': "该账号已注册！"}
                return render(request, "web/index/register.html", context)
            ob.username = request.POST['username']
            ob.nickname = request.POST['nickname']
            ob.age = request.POST['age']
            ob.sex = request.POST['sex']
            ob.avatar = 0
            ob.mobile = request.POST['mobile']

            import hashlib, random
            md5 = hashlib.md5()
            n = random.randint(100000, 999999)
            s = request.POST['password'] + str(n)
            md5.update(s.encode('utf-8'))
            password_hash = md5.hexdigest()

            # 验证重复密码
            md5 = hashlib.md5()
            s = request.POST['repassword'] + str(n)
            md5.update(s.encode('utf-8'))
            repassword_hash = md5.hexdigest()
            if repassword_hash != password_hash:
                context = {'info': "两次密码不一致！"}
                return render(request, "web/index/register.html", context)

            ob.password_hash = password_hash
            ob.password_salt = n

            ob.status = 1
            ob.create_at = datetime.now()
            ob.update_at = datetime.now()
            ob.save()
            print('注册成功')
            request.session['user'] = ob.toDict()
            return redirect(reverse("web_index"))
        else:
            context = {'info': "请同意我们的条款！"}
    except Exception as err:
        print(err)
        context = {'info': "注册失败！"}
    return render(request, "web/index/register.html", context)


# 会员退出
def logout(request):
    del request.session['user']
    return redirect(reverse('web_login'))
