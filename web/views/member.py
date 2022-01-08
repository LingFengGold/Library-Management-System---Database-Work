# 会员信息管理的视图文件

from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from myadmin.models import Member


def index(request, pIndex=1):
    umod = Member.objects
    ulist = umod.filter(status__lt=9)
    mywhere = []

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
    context = {"memberlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}

    return render(request, "myadmin/member/index.html", context)


def delete(request, mid=0):
    try:
        ob = Member.objects.get(id=uid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "删除成功！"}
    except Exception as err:
        print(err)
        context = {'info': "删除失败！"}
    return render(request, "myadmin/info.html", context)

def edit(request, mid=0):
    try:
        ob = Member.objects.get(id=uid)
        context={'member':ob}
        return render(request, "myadmin/member/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': "没有找到要修改的信息！！"}
        render(request, "myadmin/info.html", context)


def update(request, mid):
    try:
        ob = Member.objects.get(id=mid)
        ob.nickname = request.POST['nickname']

        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "修改成功！"}
    except Exception as err:
        print(err)
        context = {'info': "修改失败！"}
    return render(request, "myadmin/info.html", context)