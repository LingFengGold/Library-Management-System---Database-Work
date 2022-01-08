# 后台管理子路由文件
from django.contrib import admin
from django.urls import path
from myadmin.views import index
from myadmin.views import user, shop, category, book, member, order

urlpatterns = [
    path('', index.index, name="myadmin_index"),  # 后台首页

    # 后台管理员登录、退出路由
    path('login', index.login, name="myadmin_login"),  # 记载登录表单
    path('dologin', index.dologin, name="myadmin_dologin"),  # 执行登录
    path('logout', index.logout, name="myadmin_logout"),  # 退出

    # 员工信息管理路由
    path('user/<int:pIndex>', user.index, name="myadmin_user_index"),  # 后台首页
    path('user/add', user.add, name="myadmin_user_add"),  # 添加表单
    path('user/insert', user.insert, name="myadmin_user_insert"),  # 执行添加
    path('user/del/<int:uid>', user.delete, name="myadmin_user_delete"),  # 执行删除
    path('user/edit/<int:uid>', user.edit, name="myadmin_user_edit"),  # 加载编辑表单
    path('user/update/<int:uid>', user.update, name="myadmin_user_update"),  # 执行编辑

    # 图书馆信息管理路由
    path('shop/<int:pIndex>', shop.index, name="myadmin_shop_index"),  # 后台首页
    path('shop/add', shop.add, name="myadmin_shop_add"),  # 添加表单
    path('shop/insert', shop.insert, name="myadmin_shop_insert"),  # 执行添加
    path('shop/del/<int:sid>', shop.delete, name="myadmin_shop_delete"),  # 执行删除
    path('shop/edit/<int:sid>', shop.edit, name="myadmin_shop_edit"),  # 加载编辑表单
    path('shop/update/<int:sid>', shop.update, name="myadmin_shop_update"),  # 执行编辑

    # 图书类别信息管理路由
    path('category/<int:pIndex>', category.index, name="myadmin_category_index"),  # 后台首页
    path('category/load/<int:sid>', category.loadCategory, name="myadmin_category_load"),
    path('category/add', category.add, name="myadmin_category_add"),  # 添加表单
    path('category/insert', category.insert, name="myadmin_category_insert"),  # 执行添加
    path('category/del/<int:cid>', category.delete, name="myadmin_category_delete"),  # 执行删除
    path('category/edit/<int:cid>', category.edit, name="myadmin_category_edit"),  # 加载编辑表单
    path('category/update/<int:cid>', category.update, name="myadmin_category_update"),  # 执行编辑

    # 图书信息管理路由
    path('book/<int:pIndex>', book.index, name="myadmin_book_index"),  # 后台首页
    path('book/add', book.add, name="myadmin_book_add"),  # 添加表单
    path('book/insert', book.insert, name="myadmin_book_insert"),  # 执行添加
    path('book/del/<int:bid>', book.delete, name="myadmin_book_delete"),  # 执行删除
    path('book/edit/<int:bid>', book.edit, name="myadmin_book_edit"),  # 加载编辑表单
    path('book/update/<int:bid>', book.update, name="myadmin_book_update"),  # 执行编辑

    # 会员信息管理路由
    path('member/<int:pIndex>', member.index, name="myadmin_member_index"),  # 浏览
    path('member/del/<int:mid>', member.delete, name="myadmin_member_delete"),  # 执行删除
    path('member/edit/<int:mid>', member.edit, name="myadmin_member_edit"),  # 加载编辑表单
    path('member/update/<int:mid>', member.update, name="myadmin_member_update"),  # 执行编辑

    # 用户订单管理路由
    path('order/<int:pIndex>', order.index, name="myadmin_order_index"),  # 订单首页
    path('order/reborrow/<int:oid>', order.reborrow, name="myadmin_order_reborrow"),  # 执行续借
    path('order/return_/<int:oid>', order.return_, name="myadmin_order_return_"),  # 执行还书
    path('order/borrow/<int:oid>', order.borrow, name="myadmin_order_borrow"),  # 执行借阅
    path('order/confuse_reborrow/<int:oid>', order.confuse_reborrow, name="myadmin_order_confuseReborrow"),  # 执行拒绝续借
    path('order/confuse_return_/<int:oid>', order.confuse_return_, name="myadmin_order_confuseReturn_"),  # 执行拒绝还书
    path('order/confuse_borrow/<int:oid>', order.confuse_borrow, name="myadmin_order_confuseBorrow")]  # 执行拒绝借阅
