# 后台管理子路由文件
from django.contrib import admin
from django.urls import path
from web.views import index
from web.views import user, shop, category, book, member,order

urlpatterns = [
    path('', index.index, name="web_index"),  # 后台首页

    # 登录、退出路由
    path('login', index.login, name="web_login"),  # 记载登录表单
    path('dologin', index.dologin, name="web_dologin"),  # 执行登录
    path('register', index.register, name="web_register"),  # 注册表单
    path('doregister', index.doregister, name="web_doregister"),  # 执行登录
    path('logout', index.logout, name="web_logout"),  # 退出

    # 图书馆信息管理路由
    path('shop/<int:pIndex>', shop.index, name="web_shop_index"),  # 后台首页
    path('shop/add', shop.add, name="web_shop_add"),  # 添加表单
    path('shop/insert', shop.insert, name="web_shop_insert"),  # 执行添加
    path('shop/del/<int:sid>', shop.delete, name="web_shop_delete"),  # 执行删除
    path('shop/edit/<int:sid>', shop.edit, name="web_shop_edit"),  # 加载编辑表单
    path('shop/update/<int:sid>', shop.update, name="web_shop_update"),  # 执行编辑

    # 图书类别信息管理路由
    path('category/<int:pIndex>', category.index, name="web_category_index"),  # 后台首页
    path('category/load/<int:sid>', category.loadCategory, name="web_category_load"),
    path('category/add', category.add, name="web_category_add"),  # 添加表单
    path('category/insert', category.insert, name="web_category_insert"),  # 执行添加
    path('category/del/<int:cid>', category.delete, name="web_category_delete"),  # 执行删除
    path('category/edit/<int:cid>', category.edit, name="web_category_edit"),  # 加载编辑表单
    path('category/update/<int:cid>', category.update, name="web_category_update"),  # 执行编辑

    # 图书信息管理路由
    path('book/<int:pIndex>', book.index, name="web_book_index"),  # 后台首页
    path('book/add', book.add, name="web_book_add"),  # 添加表单
    path('book/insert', book.insert, name="web_book_insert"),  # 执行添加
    path('book/del/<int:bid>', book.delete, name="web_book_delete"),  # 执行删除
    path('book/edit/<int:bid>', book.edit, name="web_book_edit"),  # 加载编辑表单
    path('book/update/<int:bid>', book.update, name="web_book_update"),  # 执行编辑
    path('book/borrow',book.borrow,name="web_book_borrow"),#执行借书

    #用户订单管理路由
    path('order/<int:pIndex>', order.index, name="web_order_index"),  # 订单首页
    path('book/reborrow/<int:oid>', order.reborrow, name="web_order_reborrow"),  # 执行续借
    path('book/return_/<int:oid>', order.return_, name="web_order_return_"),  # 执行还书
]
