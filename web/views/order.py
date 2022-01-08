# 图书信息管理的视图文件
import os
from datetime import datetime, timedelta
import time
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myadmin.models import Category, Shop, Book, Orders
import pytz


def index(request, pIndex=1):
    umod = Orders.objects
    memberid = request.session['user']['id']

    # 取小于9的状态和当前用户的所有订单
    ulist = umod.filter(status__lt=9)
    ulist = ulist.filter(member_id=memberid)
    mywhere = []

    # 判断是否超时
    now = datetime.now().replace(tzinfo=pytz.timezone('UTC'))
    for i in ulist:
        if now > i.endtime.replace() + timedelta(hours=8) and i.return_status == 4:
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

    # 获取判断封装status搜索条件
    status = request.GET.get("status", '')
    if status != "":
        ulist = ulist.filter(status=status)
        mywhere.append("status=" + status)

    # 对id升序排序
    ulist = ulist.order_by("-starttime")

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

    context = {"orderlist": list2, 'plist': plist, 'pIndex': pIndex,
               'maxpages': maxpages, 'mywhere': mywhere, 'memberid': memberid}

    return render(request, "web/order/index.html", context)


def reborrow(request, oid):
    try:
        ob = Orders.objects.get(id=oid)
        # 只有当申请成功且未还书状态下才可以进行续借，否则报错
        if ob.borrow_status != 3 or ob.return_status != 4:
            context = {'info': "未借阅或已还书！续借申请失败！"}
            return render(request, "web/info.html", context)

        ob.borrow_status = 4
        ob.save()
        context = {'info': "续借申请成功！"}
    except Exception as err:
        print(err)
        context = {'info': "续借申请失败！"}
    return render(request, "web/info.html", context)

def return_(request, oid):
    try:
        ob = Orders.objects.get(id=oid)
        # 只有在未还书和已超时状态下才可以申请还书
        if ob.return_status != 4 and ob.return_status != 5:
            context = {'info': "未还书或已超时才可以申请还书！还书申请失败！"}
            return render(request, "web/info.html", context)
        ob.return_status = 1
        ob.save()
        context = {'info': "还书申请成功！"}
    except Exception as err:
        print(err)
        context = {'info': "还书申请失败！"}
    return render(request, "web/info.html", context)


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
    return render(request, "web/info.html", context)


def borrow(request):
    try:
        ob = Orders()

        #如果书的剩余量为0则不允许借阅
        ob2 = Book.objects.get(bid=ob.book_id)
        if ob2.number <= 0:
            context = {'info': "库存不足，申请失败！"}
            return render(request, "web/info.html", context)

        ob.shop_id = request.POST['shop_id']
        ob.member_id = request.POST['member_id']
        ob.book_id = request.POST['book_id']
        ob.borrow_status = 1
        ob.return_status = 1
        ob.status = 1
        ob.starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.endtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "申请借阅成功！"}
    except Exception as err:
        print(err)
        context = {'info': "申请借阅失败！"}
    return render(request, "web/info.html", context)


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
    return render(request, "web/info.html", context)


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
        render(request, "web/info.html", context)


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
    return render(request, "web/info.html", context)
