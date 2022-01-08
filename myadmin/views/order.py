# 图书信息管理的视图文件
import os
import time
from datetime import datetime, timedelta
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
import pytz

# Create your views here.
from myadmin.models import Category, Shop, Book, Orders, Member


def index(request, pIndex=1):
    umod = Orders.objects

    # 取小于9的状态
    ulist = umod.filter(status__lt=9)
    mywhere = []

    #判断是否超时
    now = datetime.now().replace(tzinfo=pytz.timezone('UTC'))
    for i in ulist:
        if now>i.endtime.replace()+timedelta(hours=8) and i.return_status == 4:
            i.return_status = 5
        i.save()

    # 获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        ulist = ulist.filter(name__contains=kw)
        mywhere.append("keyword=" + kw)

    # 获取并判断搜索图书类别条件
    cid = request.GET.get("category_id", None)
    if kw:
        ulist = ulist.filter(category_id=cid)
        mywhere.append("category_id=" + kw)

    # 获取并判断未已超时
    outtime_status = request.GET.get("order_outtime", '')
    if outtime_status != "":
        ulist = ulist.filter(return_status=5)
        mywhere.append("outtime_status=" + outtime_status)

    # 获取并判断未还书
    returnStatus_status = request.GET.get("order_returnStatus", '')
    if returnStatus_status != "":
        ulist = ulist.filter(return_status=4)
        mywhere.append("returnStatus_status=" + returnStatus_status)


    # 获取并判断借阅请求
    borrow_status = request.GET.get("order_borrow", '')
    if borrow_status != "":
        ulist = ulist.filter(borrow_status=1)
        mywhere.append("borrow_status=" + borrow_status)

    # 获取并判断续借请求
    reborrow_status = request.GET.get("order_reborrow", '')
    if reborrow_status != "":
        ulist = ulist.filter(borrow_status=4)
        mywhere.append("reborrow_status=" + reborrow_status)

    # 获取并判断还书请求
    return_status = request.GET.get("order_return", '')
    if return_status != "":
        ulist = ulist.filter(return_status=1)
        mywhere.append("return_status=" + return_status)

    # 对id升序排序
    ulist = ulist.order_by("-create_at")

    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(ulist, 10)  # 以每页10个数据分页
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
        cob = Book.objects.get(id=vo.book_id)
        vo.bookname = cob.name
        vo.coverpic = cob.cover_pic
        mob = Member.objects.get(id=vo.member_id)
        vo.membername = mob.nickname

    context = {"orderlist": list2, 'plist': plist, 'pIndex': pIndex,
               'maxpages': maxpages, 'mywhere': mywhere}

    return render(request, "myadmin/order/index.html", context)


# 同意借阅
def borrow(request, oid):
    try:
        ob = Orders.objects.get(id=oid)
        ob.borrow_status = 3
        ob.return_status = 4
        ob.starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        end = datetime.now() + timedelta(minutes=3)
        ob.endtime = end.strftime('%Y-%m-%d %H:%M:%S')

        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()

        ob2 = Book.objects.get(id=ob.book_id)
        ob2.number = ob2.number - 1
        ob2.save()
        context = {'info': "同意借阅成功！"}
    except Exception as err:
        print(err)
        context = {'info': "同意借阅失败！"}
    return render(request, "myadmin/info.html", context)


# 拒绝借阅
def confuse_borrow(request, oid):
    try:
        ob = Orders.objects.get(id=oid)
        if ob.borrow_status != 1:
            context = {'info': "未申请借书！拒绝借书失败！"}
            return render(request, "myadmin/info.html", context)
        ob.borrow_status = 2
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "拒绝借阅成功！"}
    except Exception as err:
        print(err)
        context = {'info': "拒绝借阅失败！"}
    return render(request, "myadmin/info.html", context)


# 同意续借
def reborrow(request, oid):
    try:
        ob = Orders.objects.get(id=oid)
        ob.borrow_status = 5

        end = datetime.now() + timedelta(hours=3)
        ob.endtime = end.strftime('%Y-%m-%d %H:%M:%S')

        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "同意续借成功！"}
    except Exception as err:
        print(err)
        context = {'info': "同意续借失败！"}
    return render(request, "myadmin/info.html", context)


# 拒绝续借
def confuse_reborrow(request, oid):
    try:
        ob = Orders.objects.get(id=oid)
        if ob.borrow_status != 4:
            context = {'info': "未申请续借！拒绝续借失败！"}
            return render(request, "myadmin/info.html", context)
        ob.borrow_status = 6
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "拒绝续借成功！"}
    except Exception as err:
        print(err)
        context = {'info': "拒绝续借失败！"}
    return render(request, "myadmin/info.html", context)


# 同意还书
def return_(request, oid):
    try:
        ob = Orders.objects.get(id=oid)
        ob.return_status = 3
        ob.endtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        ob2 = Book.objects.get(id=ob.book_id)
        ob2.number = ob2.number + 1
        ob2.save()
        context = {'info': "同意还书成功！"}
    except Exception as err:
        print(err)
        context = {'info': "同意还书失败！"}
    return render(request, "myadmin/info.html", context)


# 拒绝还书
def confuse_return_(request, oid):
    try:
        ob = Orders.objects.get(id=oid)
        if ob.return_status != 1:
            context = {'info': "未申请还书！拒绝还书失败！"}
            return render(request, "myadmin/info.html", context)
        ob.return_status = 4
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "拒绝还书成功！"}
    except Exception as err:
        print(err)
        context = {'info': "拒绝还书失败！"}
    return render(request, "myadmin/info.html", context)


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
        return render(request, "web/book/edit.html", context)
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
