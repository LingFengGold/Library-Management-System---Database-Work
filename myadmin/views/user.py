# 员工信息管理的视图文件

from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from myadmin.models import User


def index(request, pIndex=1):
    umod = User.objects
    ulist = umod.filter(status__lt=9)
    mywhere = []

    # 获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        ulist = ulist.filter(Q(username__contains=kw) | Q(nickname__contains=kw))
        mywhere.append("keyword=" + kw)

    # 获取判断封装status搜索条件
    status = request.GET.get("status", '')
    if status != "":
        ulist = ulist.filter(status=status)
        mywhere.append("status=" + status)
    ulist = ulist.order_by("id")
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(ulist, 3)  # 以每页5个数据分页
    maxpages = page.num_pages
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)
    plist = page.page_range
    context = {"userlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}

    return render(request, "myadmin/user/index.html", context)


def add(request):
    return render(request, "myadmin/user/add.html")


def insert(request):
    try:
        ob = User()
        ob.username = request.POST['username']
        ob.nickname = request.POST['nickname']

        # 获取密码并md5
        import hashlib, random
        md5 = hashlib.md5()
        n = random.randint(100000, 999999)
        s = request.POST['password'] + str(n)
        md5.update(s.encode('utf-8'))
        password_hash=md5.hexdigest()

        #验证重复密码
        md5 = hashlib.md5()
        s = request.POST['repassword'] + str(n)
        md5.update(s.encode('utf-8'))
        repassword_hash=md5.hexdigest()
        if repassword_hash!=password_hash:
            context = {'info': "两次密码不一致！"}
            return render(request, "myadmin/info.html", context)

        ob.password_hash = password_hash
        ob.password_salt = n

        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "添加成功！"}
    except Exception as err:
        print(err)
        context = {'info': "添加失败！"}
    return render(request, "myadmin/info.html", context)


def delete(request, uid=0):
    try:
        ob = User.objects.get(id=uid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "删除成功！"}
    except Exception as err:
        print(err)
        context = {'info': "删除失败！"}
    return render(request, "myadmin/info.html", context)


def edit(request, uid=0):
    try:
        ob = User.objects.get(id=uid)
        context={'user':ob}
        return render(request, "myadmin/user/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': "没有找到要修改的信息！！"}
        render(request, "myadmin/user/edit.html", context)


def update(request, uid):
    try:
        ob = User.objects.get(id=uid)
        ob.nickname = request.POST['nickname']
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "修改成功！"}
    except Exception as err:
        print(err)
        context = {'info': "修改失败！"}
    return render(request, "myadmin/info.html", context)
