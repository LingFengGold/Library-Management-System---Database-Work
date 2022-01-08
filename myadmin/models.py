from django.db import models
from datetime import datetime


# Create your models here.

# 员工账号信息模型
class User(models.Model):
    username = models.CharField(max_length=50)  # 员工账号
    nickname = models.CharField(max_length=50)  # 昵称
    password_hash = models.CharField(max_length=100)  # 密码
    password_salt = models.CharField(max_length=50)  # 密码干扰值
    status = models.IntegerField(default=1)  # 状态1正常 / 2禁用 / 9删除
    create_at = models.DateTimeField(default=datetime.now)  # 创建时问
    update_at = models.DateTimeField(default=datetime.now)  # 修改时间

    def toDict(self):
        return {'id': self.id, 'username': self.username, 'nickname': self.nickname,
                'password_hash': self.password_hash, 'password_salt': self.password_salt, 'status': self.status,
                'create_at': self.create_at.strftime('%Y-%m-%d %H:%M:%S'),
                'update_at': self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "user"


# 图书馆信息模型
class Shop(models.Model):
    name = models.CharField(max_length=255)  # 图书馆名称
    cover_pic = models.CharField(max_length=255)  # 封面图片
    banner_pic = models.CharField(max_length=255)  # 图标Logo
    address = models.CharField(max_length=255)  # 图书馆地址
    phone = models.CharField(max_length=255)  # 联系电话
    status = models.IntegerField(default=1)  # 状态:1正常/2暂停/9删除
    create_at = models.DateTimeField(default=datetime.now)  # 创建时间
    update_at = models.DateTimeField(default=datetime.now)  # 修改时间

    def toDict(self):
        shopname = self.name.split("-")
        return {'id': self.id, 'name': shopname[0], 'shop': shopname[1], 'cover_pic': self.cover_pic,
                'banner_pic': self.banner_pic, 'address': self.address, 'phone': self.phone, 'status': self.status,
                'create_at': self.create_at.strftime('%Y-%m-%d %H:%M:%S'),
                'update_at': self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "shop"  # 更改表名


# 图书分类信息模型
class Category(models.Model):
    shop_id = models.IntegerField()  # 图书馆id
    name = models.CharField(max_length=50)  # 分类名称
    status = models.IntegerField(default=1)  # 状态:1正常/9删除
    create_at = models.DateTimeField(default=datetime.now)  # 创建时间
    update_at = models.DateTimeField(default=datetime.now)  # 修改时间

    class Meta:
        db_table = "category"  # 更改表名


# 图书信息模型
class Book(models.Model):
    shop_id = models.IntegerField()  # 图书id
    category_id = models.IntegerField()  # 图书分类id
    cover_pic = models.CharField(max_length=50)  # 图书图片
    name = models.CharField(max_length=50)  # 图书名称
    author = models.CharField(max_length=50)  # 作者名称
    price = models.FloatField()  # 图书单价
    number = models.IntegerField(default=0)  # 图书数量
    status = models.IntegerField(default=1)  # 状态:1正常/2停售/9删除
    create_at = models.DateTimeField(default=datetime.now)  # 创建时间
    update_at = models.DateTimeField(default=datetime.now)  # 修改时间

    def toDict(self):
        return {'id': self.id, 'shop_id': self.shop_id, 'category_id': self.category_id, 'cover_pic': self.cover_pic,
                'name': self.name, 'author': self.author, 'number': self.number, 'price': self.price,
                'status': self.status,
                'create_at': self.create_at.strftime('%Y-%m-%d %H:%M:%S'),
                'update_at': self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "book"  # 更改表名


# 会员信息模型
class Member(models.Model):
    nickname = models.CharField(max_length=50)  # 昵称
    age = models.IntegerField()  # 年龄
    sex = models.CharField(max_length=50)  # 性别
    avatar = models.CharField(max_length=255)  # 头像
    mobile = models.CharField(max_length=50)  # 电话
    status = models.IntegerField(default=1)  # 状态:1正常/2禁用/9删除
    create_at = models.DateTimeField(default=datetime.now)  # 创建时间
    update_at = models.DateTimeField(default=datetime.now)  # 修改时间
    username = models.CharField(max_length=50)  # 员工账号
    password_hash = models.CharField(max_length=100)  # 密码
    password_salt = models.CharField(max_length=50)  # 密码干扰值

    def toDict(self):
        return {'id': self.id, 'nickname': self.nickname, 'avatar': self.avatar, 'mobile': self.mobile,
                'status': self.status, 'sex': self.sex, 'age': self.age,
                'create_at': self.create_at.strftime('%Y-%m-%d %H:%M:%S'),
                'update_at': self.update_at.strftime('%Y-%m-%d %H:%M:%S'),
                'password_hash': self.password_hash, 'username': self.username,
                'password_salt': self.password_salt, }

    class Meta:
        db_table = "member"  # 更改表名


# 订单模型
class Orders(models.Model):
    shop_id = models.IntegerField()  # 图书馆id号
    member_id = models.IntegerField()  # 会员id
    book_id = models.IntegerField()  # 图书id
    borrow_status = models.IntegerField(default=1)  # 借书状态:1申请借书/2申请失败/3申请成功/4申请续借/5续借成功/6续借失败/7无效
    return_status = models.IntegerField(default=4)  # 还书状态:1申请还书/2申请失败/3已还书/4未还书/5已超时/6无效
    status = models.IntegerField(default=1)  # 状态:1正常/2禁用/9删除
    endtime = models.DateTimeField(default=datetime.now)  # 还书时间
    starttime = models.DateTimeField(default=datetime.now)  # 结束时间
    create_at = models.DateTimeField(default=datetime.now)  # 创建时间
    update_at = models.DateTimeField(default=datetime.now)  # 修改时间

    def toDict(self):
        return {'id': self.id, 'shop_id': self.shop_id, 'member_id': self.member_id,
                'book_id': self.book_id, 'borrow_status': self.borrow_status,
                'return_status': self.return_status, 'status': self.status,
                'endtime': self.endtime.strftime('%Y-%m-%d %H:%M:%S'),
                'starttime': self.starttime.strftime('%Y-%m-%d %H:%M:%S'),
                'create_at': self.create_at.strftime('%Y-%m-%d %H:%M:%S'),
                'update_at': self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "orders"  # 更改表名

# #订单详情模型
# class OrderDetail(models.Model):
#     order_id = models.IntegerField()  #订单id
#     #product_id = models.IntegerField()  #书籍id
#     book = models.ForeignKey('Book',on_delete=models.CASCADE) # 多对一
#     book_name = models.CharField(max_length=50) #图书名称
#     price = models.FloatField()     #单价
#     quantity = models.IntegerField()  #数量
#     status = models.IntegerField(default=1) #状态:1正常/9删除
#
#     class Meta:
#         db_table = "order_detail"  # 更改表名
#
#
# # 还书信息模型
# class Payment(models.Model):
#     order_id = models.IntegerField()  #订单id号
#     member_id = models.IntegerField() #会员id
#     money = models.FloatField()     #支付金额
#     type = models.IntegerField()      #付款方式：1会员付款/2收银收款
#     bank = models.IntegerField(default=1) #收款银行渠道:1微信/2余额/3现金/4支付宝
#     status = models.IntegerField(default=1) #支付状态:1未支付/2已支付/3已退款
#     create_at = models.DateTimeField(default=datetime.now)  #创建时间
#     update_at = models.DateTimeField(default=datetime.now)  #修改时间
#
#     class Meta:
#         db_table = "payment"  # 更改表名
