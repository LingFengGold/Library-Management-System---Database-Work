# 图书信息管理的视图文件
import os
from datetime import datetime
import time
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myadmin.models import Category, Shop, Book


def index(request, pIndex=1):
    umod = Book.objects
    ulist = umod.filter(status__lt=9)
    mywhere = []

    # 获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        ulist = ulist.filter(name__contains=kw)
        mywhere.append("keyword=" + kw)

    # 获取判断封装status搜索条件
    status = request.GET.get("status", '')
    if status != "":
        ulist = ulist.filter(status=status)
        mywhere.append("status=" + status)

    # 对id升序排序
    ulist = ulist.order_by("id")

    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(ulist, 6)  # 以每页10个数据分页
    maxpages = page.num_pages
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)
    plist = page.page_range

    # 遍历当前图书分类信息并封装到对应的店铺和菜品类别信息
    for vo in list2:
        sob = Shop.objects.get(id=vo.shop_id)
        vo.shopname = sob.name
        cob = Category.objects.get(id=vo.category_id)
        vo.categoryname = cob.name

    context = {"booklist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}

    return render(request, "myadmin/book/index.html", context)


def add(request):
    # 获取当前图书馆
    slist = Shop.objects.values("id", 'name')
    context = {"shoplist": slist}
    # clist = Shop.objects.values("id", 'name')
    # context["categorylist"]= clist
    return render(request, "myadmin/book/add.html", context)


def insert(request):
    try:
        # 图书馆封面图片的上传处理
        myfile = request.FILES.get("cover_pic", None)
        if not myfile:
            return HttpResponse("没有图书馆封面上传文件信息")
        cover_pic = str(time.time()) + "." + myfile.name.split('.').pop()
        destination = open("./static/uploads/book/" + cover_pic, "wb+")  # 此处需要修改路径
        for chunk in myfile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

        ob = Book()
        ob.shop_id = request.POST['shop_id']
        ob.category_id = request.POST['category_id']
        ob.name = request.POST['name']
        ob.price = request.POST['price']
        ob.author = request.POST['author']
        ob.number = request.POST['number']
        ob.cover_pic = cover_pic
        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "添加成功！"}
    except Exception as err:
        print(err)
        context = {'info': "添加失败！"}
    return render(request, "myadmin/info.html", context)


def delete(request, bid=0):
    try:
        ob = Book.objects.get(id=bid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "删除成功！"}
    except Exception as err:
        print(err)
        context = {'info': "删除失败！"}
    return render(request, "myadmin/info.html", context)


def edit(request, bid=0):
    try:
        ob = Book.objects.get(id=bid)
        context = {'book': ob}
        slist = Shop.objects.values("id", 'name')
        context["shoplist"] = slist
        clist = Category.objects.values("id", 'name')
        context["categorylist"] = clist
        return render(request, "myadmin/../../templates/web/book/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': "没有找到要修改的信息！！"}
        render(request, "myadmin/info.html", context)


def update(request, bid):
    try:
        # 获取原图片
        oldpicname = request.POST['oldpicname']
        ##图片的上传处理
        myfile = request.FILES.get("cover_pic", None)
        if not myfile:
            cover_pic = oldpicname
        else:
            cover_pic = str(time.time()) + "." + myfile.name.split('.').pop()
            destination = open("./static/uploads/book/" + cover_pic, "wb+")
            for chunk in myfile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()

        ob = Book.objects.get(id=bid)
        ob.shop_id = request.POST['shop_id']
        ob.category_id = request.POST['category_id']
        ob.name = request.POST['name']
        ob.price = request.POST['price']
        ob.author = request.POST['author']
        ob.number = request.POST['number']
        ob.cover_pic = cover_pic
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "修改成功！"}

        # 判断并删除老照片
        if myfile:
            os.remove("./static/uploads/book/" + oldpicname)

    except Exception as err:
        print(err)
        context = {'info': "修改失败！"}
        # 判断并删除新照片
        if myfile:
            os.remove("./static/uploads/book/" + cover_pic)
    return render(request, "myadmin/info.html", context)
