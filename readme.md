# 2021 图书馆管理系统-SDU数据库大作业

## 前言

​	近年来，随着国民生活水平、生活质量的迅速提高，科学技术的飞速发展，我们已步入信息化、数字化的时代，web办公、“互联网+”已经成为时代的主流。而图书馆是人民群众满足文化需求的重要途径，是我们老百姓有书畅读的保障，与我们的生活密切相关。工作效率对于图书馆来说十分重要，图书馆访问量大，需求性强。因此，图书馆需要更直接方便快捷的管理方法来应对日常的工作事务，以提高整个图书馆的运作效率。于是，图书馆对管理信息系统的需求越来越迫切。一套好的信息系统在全面提高图书馆的为人民服务功能，提高图书馆整体工作效率，为读者提供方便快捷全面的服务等方面都能发挥出重要作用。而图书馆信息管理系统作为整个图书馆管理系统的子系统，同样非常重要。它的设计的操作性和维护性的好坏将直接影响整个系统，乃至整个图书馆的运行效率。	

​	本项目就是研究图书馆信息管理系统的数据库构建过程。该数据库展现了借书过程中的基本信息与基本流程，主要包括会员、员工的基本信息资料，办理注册登录，图书馆、图书分类、图书的基本信息资料，图书馆的信息括图书馆的地址、电话、封面照片、logo照片等内容的录入编辑修改，以及图书的基本信息资料，包括图书的所属图书馆、图书分类、图书名称、图书封面、图书价格、图书作者等信息的录入编辑修改。会员借阅图书、归还图书、续借图书等功能，同时管理员还可以在后台审核这些操作。

## 一、系统开发平台

### 1.1 开发平台简介

​	本住院管理系统采用B-S架构，使用Python的技术路线，遵守Django MTV框架模型。

​	Model模型层使用数据库作为持久性储存结构，选用的后台数据库是MySQL8.0.27。这是业界领先的开源数据库，在开源产品中具有仅次于Apache服务器的市场占有率。本数据库开放源代码，具有免费使用，比较稳定的特点，适合于小型系统的持久性存储。

​	Template, 模板 与MVC中的V类似，负责如何显示数据（产生html界面）使用HTML、CSS、JavaScript技术。这是使用最广泛的浏览器界面技术。图书管理系统中严格控制界面代码中的业务逻辑部分，实现了很好的业务和表现的分离。

​	View视图层实现了对数据库中数据的增删查改的具体方法。界面获取的数据通过调用相应方法进行数据的封装和与数据库的交互，从而实现业务逻辑和表现的完全分离。

### 1.2 开发语言：Python+Django 3.2.9

​	用Python做设计流程清晰、结构合理，有良好的可扩充性和耦合性。

​	Python版本3.9

### 1.3 开发工具：PyCharm、VsCode 1.62.3

### 1.4 数据库: MySQL 8.0.27

​	MySQL是业界领先的开源数据库，在开源产品中具有仅次于Apache服务器的市场占有率。本数据库开放源代码，具有免费使用，比较稳定的特点，适合于小型系统的持久性存储。

​	连接数据库：PyMySQL 1.0.2

### 1.5 操作系统：macOSMonterey 12.1

 

## 二、数据库规划

### 2.1 任务陈述

​	图书馆管理系统是一个图书馆不可缺少的部分,它的内容对于图书馆的管理者和借阅书籍的读者来说都至关重要。随着图书馆设施的普及，读者数量急剧增加，有关读者的各种信息量也成倍增长。面对庞大的信息量需要有图书馆管理系统来提高读者管理工作的效率。一个完善的图书馆管理系统能够极大地提高读者信息管理的效率,具有检索迅速、查找方便、可靠性高、存储量大、更新快、寿命长、成本低等优点。

​	本图书馆管理系统包括用户界面和后台管理界面两大主页面。

​	页面中包含读者信息注册登录管理、图书馆信息管理、图书分类信息管理、图书信息管理、员工信息管理、会员信息管理、会员借阅归还管理、管理员审核系统八大模块并且及时记录存储各个环节信息的变更，以便管理、查询、显示、输出。

​	本系统因为考虑到本身系统的特殊性，所以本系统只有管理员模式一种。管理员可以拥有完全的权限管理系统，可以完成对图书馆、图书分类、图书信息、会员信息、员工的查询，并且完成图书馆信息的增删改查、图书分类信息的增删改查、图书信息的增删改查、会员信息的增删改查、员工信息的增删改查、审核读者借阅归还续借请求的操作。

## 三、系统定义

###  3.1 系统边界

系统边界描述数据库系统和企业信息系统的其他部分的接口，是信息系统内部构成元素与外部有联系实体之间的信息关系的描述与分割。它并不需要在它们之间划一条物理边界，而只需要弄清它们之间信息输入与输出的分割。

本数据库系统共包括读者信息注册登录管理、图书馆信息管理、图书分类信息管理、图书信息管理、员工信息管理、会员信息管理、会员借阅归还管理、管理员审核系统八大模块并且及时记录存储各个环节信息的变更，以便管理、查询、显示、输出。

### 3.2 用户视图 

管理员（Administrator）用户视图

（1） 会员管理：

查询、添加、修改会员信息。

（2） 员工管理：

查询、修改、增加、删除员工信息。

（3） 图书馆管理：

查询、修改、增加、删除图书馆信息。

（4） 图书分类管理：

查询、修改、增加、删除图书分类信息

（5） 图书管理：

查询、修改、增加、删除图书信息。

（6） 订单管理：

管理、审核（借阅、归还、续借）订单

 

用户（User）视图

（1）图书馆管理：

查询图书馆信息。

（2）图书分类管理：

查询图书分类信息。

（3）图书信息管理：

查询图书信息信息。

（4）订单管理：

查询订单信息、更改订单状态。

 

## 四、需求分析

### 4.1 用户需求说明

#### 4.1.1 数据需求

其中需求数据为：

##### 1、员工的基本信息记录：

员工ID、员工姓名、员工昵称、当前状态、添加时间、修改时间、密码

##### 2、会员基本信息记录：

会员ID、会员姓名、会员昵称、会员年龄、会员性别、会员手机号、当前状态、添加时间、修改时间、密码

##### 3、图书馆基本信息记录：

图书馆ID、图书馆名称、图书馆封面图片、LOGO图片、联系电话、地址、当前状态、添加时间、修改时间

##### 4、图书分类信息记录：

图书分类ID、类别名称、当前状态、添加时间、修改时间

##### 5、图书信息记录：

图书ID、图书馆名称、图书分类、图片、图书名称、作者、单价、数量、状态、添加时间

##### 6、订单信息记录：

订单ID、图书馆名称、图书名称、图片、借阅、还书、订单状态、借阅时间、归还时间、姓名

#### 4.1.2 事务需求

##### 1、 数据录入：

（1） 录入员工的基本信息：

员工ID、员工姓名、员工昵称、当前状态、添加时间、修改时间、密码

（2） 录入会员的基本信息：

会员ID、会员姓名、会员昵称、会员年龄、会员性别、会员手机号、当前状态、添加时间、修改时间、密码

（3） 录入图书馆基本信息：

图书馆ID、图书馆名称、图书馆封面图片、LOGO图片、联系电话、地址、当前状态、添加时间、修改时间

（4） 录入图书分类信息：

图书分类ID、类别名称、当前状态、添加时间、修改时间

（5） 录入图书信息：

图书ID、图书馆名称、图书分类、图片、图书名称、作者、单价、数量、状态、添加时间

##### 2、 数据更新/删除：

（1） 员工信息的更新、删除

（2） 会员信息的更新、删除

（3） 图书馆信息的更新、删除

（4） 图书分类的更新、删除

（5） 图书信息的更新、删除

（6） 订单信息的更新

##### 3、 数据查看：

管理员用户视图下：

（1）后台操作：登录、退出

（2）员工信息管理：添加、删除、修改、重置密码、查看、分配图书馆

（3）图书馆信息管理：添加、删除、修改、查看图书馆信息

（4）图书分类信息查询：添加、删除、修改、查看书籍类别信息

（5）图书信息管理：添加、删除、修改、查看图书信息

（6）会员信息管理：查看、修改会员状态、重置密码

（7）借书记录信息管理：查看记录、记录详情、审核订单

（8）其他拓展：权限管理、系统配置等、

前台图书馆借还书界面：

（1）图书馆借书：登录与退出

（2）图书馆借书首页：展示当前图书馆的基本信息、图书分类、图书信息

（4）借还书订单管理：浏览借阅记录列表、处理借阅记录

（5）其他拓展：汇总数据展示：借阅统计等

### 4.2 系统需求说明 

该图书管理系统需要较强的数据处理功能，理论上应该能够容纳上万人的数据资料，并且在搜索方面理应具有较快的响应速度，能够处理多方面的数据请求。系统能够有效的处理各种异常，具有较好的健壮性。

#### 4.2.1 初始数据库大小

（1） 大约有3个图书馆，每个图书馆有大约4个图书分类，每个图书分类下有10本书，每种书均有10本。

（2） 每个图书馆有1个管理员。

#### 4.2.2 网络和共享需求

（1） 必须能够支持至少60名用户同时访问，需要考虑这么大数量并发访问的许可需求。

#### 4.2.3 性能

高峰期：每天的上午、下午

（1） 单个记录查询时间少于1秒，高峰期少于5秒

（2） 多个记录查询时间少于5秒，高峰期少于10秒

（3） 更新/保存记录时间少于1秒，高峰期少于5秒

#### 4.2.4 安全性

（1） 数据库必须有口令保护

（2） 每个用户分配特定的用户视图所应有的访问权限

（3） 用户只能在适合他们完成工作需要的窗口中看到需要的数据

#### 4.2.5 备份和恢复

每天24点备份

#### 4.2.6 用户界面

菜单驱动，联机帮助

#### 4.2.7 法律问题

对用户信息管理，遵守法律

 

## 五、数据库逻辑设计

### 5.1 ER图

该ER图包括会员、管理员、借书、订单、图书馆、图书分类六个实体和用管理、借书、还书、属于、含有、位于、审核、核对八个联系。

### 5.2 数据字典

#### 5.2.1 从数据字典中抽取出来的系统实体描述： 

（1）员工（id号、账号、昵称、密码、密码干扰、状态、添加时间、修改时间） 

（2）会员（id号、账号、昵称、头像、年龄、性别、电话、状态、添加时间、修改时间） 

（3）图书馆（id号、图书馆名称、封面图片、图标logo、图书馆地址、联系电话、状态、添加时间、修改时间） 

（4）书籍类别（id号、图书馆id、类别名称、状态、添加时间、修改时间） 

（5）书籍（id号、图书馆id、类别id、图书图片、图书名称、单价、状态、添加时间、修改时间） 

（6）订单详情（id号、图书馆id、会员id、图书id、借阅状态、归还状态、状态、借书时间、还书时间、添加时间、修改时间） 

订单状态含义：

borrow_status = models.IntegerField(default=1)  

# 借书状态：1申请借书/2申请失败/3申请成功/4申请续借/5续借成功/6续借失败/7无效

return_status = models.IntegerField(default=4)  

# 还书状态：1申请还书/2申请失败/3已还书/4未还书/5已超时/6无效

status = models.IntegerField(default=1)  

# 状态：1正常/2禁用/9删除

 

####  5.2.2 从数据字典中抽取出来的联系的描述：

| 实体     | 多样性 | 联系 | 多样性 | 实体     |
| -------- | ------ | ---- | ------ | -------- |
| 会员     | n      | 管理 | 1      | 管理员   |
| 会员     | 1      | 还书 | n      | 图书     |
| 会员     | 1      | 借书 | n      | 图书     |
| 管理员   | 1      | 审核 | n      | 图书     |
| 管理员   | 1      | 核对 | n      | 图书     |
| 图书     | n      | 属于 | 1      | 图书分类 |
| 图书     | n      | 位于 | 1      | 图书馆   |
| 图书分类 | n      | 含有 | 1      | 图书馆   |

 

 

## 六、数据库物理设计

### 6.1 索引

数据库中的索引：

| 表名     | 主键       | 外键                 |
| -------- | ---------- | -------------------- |
| 员工     | 员工ID     |                      |
| 会员     | 会员ID     |                      |
| 图书馆   | 图书馆ID   |                      |
| 图书分类 | 图书分类ID | 图书馆ID             |
| 图书     | 图书ID     | 图书馆ID、图书分类ID |
| 订单     | 订单ID     | 图书馆ID、会员ID     |

### 6.2 视图

此环节设计在数据库应用生命周期的需求分析和收集阶段标识的用户视图。通常，视图使用SQL或类似QBE的工具创建。例如查询id为101会员的全部信息：

CREATE VIEW View

AS SELECT 

FROM Member

WHERE id = 101；

### 6.3 安全机制

#### 6.3.1 系统安全

1、本图书馆管理系统提供了充足的异常处理机制，能够捕获由各种错误引发的异常(如：输入数据类型与数据库要求类型不一致、登录过程中密码错误、注册过程中账号已被使用等等)。

2、管理员输入信息如果与数据库已有信息重复，则提示管理者重新输入

#### 6.3.2 数据安全

1、进入后台管理界面会强制跳转到登录界面，输入管理员ID与密码。只有管理员才进入本系统实现图书馆信息管理的一系列流程，以确保数据库不被随意更改，保证数据安全。

2、本系统只有管理员身份可以进入后台，在完成各类数据的增删改查等操作后需要更新其他的有关的联系表，这些都是通过事务实现的，很好的保护了关系型数据库的强一致性，体现了数据安全。

3、使用MD5加密算法对用户注册时输入的密码进行机密处理，使得即使管理员也无法获取用户的密码，增强了用户的隐私性和数据安全性。

### 6.4 其他

规范化产生一个结构上一致且最小冗余的逻辑数据库设计，但是，规范化的数据库设计有时不能提供最大的处理效率。所以我们愿意接收规范化设计方面的一些损失而实现更好的性能。



## 七、应用程序设计

### 7.1 功能模块

该图书管理信息系统共有员工信息管理、会员信息管理、图书馆信息管理、图书分类信息管理、图书信息管理、订单申请、订单审核七大功能模块，功能模块具体实现如下：

#### 7.1.1员工信息管理

（1）进入员工信息管理页面

（2）搜索待修改员工昵称或新增员工

（2）找到待修改员工信息的员工所在位置

（3）点击编辑或者删除

（5）如果编辑，则需输入修改的员工昵称、状态，员工账号默认不可修改。

（6）如果删除，则会将该员工的账号状态调整为禁用状态，并且不再显示在视图中。

（7）如果添加员工，则需输入员工账号、昵称、密码、重复密码。

（8）完成员工信息添加、编辑以及相关表的更新

#### 7.1.2 图书馆信息管理

（1）进入图书馆信息管理

（2）搜索图书馆名称或新增图书馆

（3）找到待修改图书馆信息的图书馆所在位置

（4）点击编辑或者删除

（5）如果编辑，则需输入修改的图书馆名称、电话、地址、营业状态、图书馆封面、图书馆LOGO

（6）如果删除，则会将该图书馆的状态调整为禁用状态，并且不再显示在视图中。

（7）如果添加图书馆，则需输入图书馆名称、联系电话、具体地址、图书馆封面、图书馆LOGO

（8）完成图书馆信息添加、编辑以及相关表的更新

#### 7.1.3 图书分类信息管理

（1）进入图书馆信息管理

（2）搜索图书分类名称或新增图书分类

（3）找到待修改图书分类的图书馆所在位置

（4）点击编辑或者删除

（5）如果编辑，则需输入修改的图书馆名称、类别名称、状态

（6）如果删除，则会将该图书分类的状态调整为禁用状态，并且不再显示在视图中。

（7）如果添加图书分类，则需输入图书馆名称、类别名称

（8）完成图书分类信息添加、编辑以及相关表的更新

#### 7.1.4 图书信息管理

（1）进入图书信息管理

（2）搜索图书名称或新增图书

（3）找到待修改图书所在位置

（4）点击编辑或者删除

（5）如果编辑，则需输入修改的图书馆名称、图书分类、图书名称、单价、作者、数量、图书封面

（6）如果删除，则会将该图书的状态调整为禁用状态，并且不再显示在视图中

（7）如果添加图书，则需输入图书馆名称、图书分类、图书名称、单价、作者、数量、图书封面

  （8）完成图书信息添加、编辑以及相关表的更新。

#### 7.1.5 会员信息管理

（1）进入会员信息管理

（2）搜索会员名称

（3）查看会员信息

#### 7.1.6 图书借阅订单审核核心模块

（1）按照已超时、未还书、借阅请求、续借请求、还书请求五类进行分类

（2）点击同意借阅、拒绝借阅、同意续借、拒绝续借、同意还书、拒绝还书完成相应操作。

（3）若借阅状态不是申请成功，则点击续借和还书相关按钮会弹出报错信息。

（4）若还书状态为未还书时，可以点击续借和还书相关按钮，同意借阅按钮会弹出报错信息。

（5）系统会根据借阅状态时间和归还时间自动判断是否超时。

（6）更新相关表的信息

 

### 7.2 界面设计

#### 7.2.1 注册界面（用户）

​	若用户未注册，则可以点击“注册一个新的账号”进入注册界面。注册账号需要输入的信息有账号、昵称、年龄、性别、电话、密码、重复密码，系统会检查两次输入的密码是否一致，并且会对密码进行MD5加密。 

#### 7.2.2 登录界面
​	用户登录界面：http://127.0.0.1:8000/login

​	用户在登录界面输入用户名和密码并经过系统验证后，可以进入图书馆管理系统-用户界面进行相关操作（账号密码为注册所用的值）。 

#### 7.2.3 主服务界面（用户）

​	在输入正确的账号密码后进入主服务界面，主服务界面左侧为导航栏，用户可以查看图书馆、图书分类、图书信息，并且进行订单管理。主界面上方也有导航栏，可以点击后台管理进入后台，最右侧可以使界面全屏、查看个人信息。  

#### 7.2.4 图书馆界面（用户）

​	用户可以在导航栏点击图书馆进入图书馆信息界面，查看现有的图书馆信息。图书馆信息表会列出图书馆ID、图书馆名称、封面图片、LOGO图片、联系电话、地址、当前状态等信息，提供翻页、搜索等便利方法。

#### 7.2.5 图书分类界面（用户）

用户可以在导航栏点击图书馆进入图书分类界面，查看现有的图书分类信息。图书分类信息表会列出图书分类ID、图书馆名称、类别名称，提供翻页、搜索等便利方法。 

#### 7.2.6 图书信息界面（用户）

​	用户可以在导航栏点击图书信息进入图书借阅界面，查看现有的图书信息。图书分类信息表会列出图书ID、图书馆名称、图书分类、图书封面图片、作者、单价、剩余数量、状态。提供翻页、搜索等便利方法。

​	用户点击申请借阅即可完成借阅申请，用户可以到订单管理界面查看借阅申请是否被通过，此时若该图书的剩余数量等于0则会弹出报错信息。 

#### 7.2.7 图书借阅订单界面（用户）

​	用户可以在导航栏点击订单管理进入订单信息表界面，查看现有的订单信息。图书订单信息表会列出订单ID、图书馆名称、图书名称、图书封面图片、借阅状态、还书状态、订单状态、借阅时间、归还时间，提供翻页、搜索等便利方法。

​	若申请成功且未还书，用户可以点击续借提出续借申请。

​	若未还书或者已超时，用户可以点击还书提出还书申请。 

#### 7.2.8 登录界面（管理员）

​	管理员登录界面：http://127.0.0.1:8000/myadmin/login

​	管理员在登录界面输入用户名和密码并经过系统验证后，可以进入图书馆管理系统-后台界面进行相关操作（账号密码为预设的值）。 

#### 7.2.9 主服务界面（管理员）

​	在输入正确的账号密码后进入主服务界面，主服务界面左侧为导航栏，管理员可以查看员工、图书馆、图书分类、图书信息，并且进行订单、会员管理。主界面上方也有导航栏，可以点击用户首页进入用户界面，最右侧可以使界面全屏、查看个人信息。 

#### 7.2.10 员工管理（管理员）

​	管理员可以在导航栏点击员工管理进入员工管理信息界面，查看现有的员工信息。员工信息表会列出员工ID、员工名称、员工昵称、当前状态、添加时间、修改时间等信息，提供翻页、搜索等便利方法。

​	管理员可以点击编辑、删除、添加员工进行进一步管理。  

#### 7.2.11 图书馆管理（管理员）

​	管理员可以在导航栏点击图书馆管理进入图书馆管理信息界面，查看现有的图书馆信息。图书馆信息表会列出图书馆ID、图书馆名称、图书馆封面照片、图书馆LOGO照片、联系电话、地址、当前状态、添加时间、修改时间等信息，提供翻页、搜索等便利方法。

​	管理员可以点击编辑、删除、添加图书馆进行进一步管理。 

#### 7.2.12 图书馆分类管理（管理员）

​	管理员可以在导航栏点击图书分类进入图书分类管理信息界面，查看现有的图书分类信息。图书分类信息表会列出图书分类ID、图书馆名称、类别名称、当前状态、添加时间、修改时间等信息，提供翻页、搜索等便利方法。

​	管理员可以点击编辑、删除、添加图书分类进行进一步管理。  

#### 7.2.13 图书信息管理（管理员）

​	管理员可以在导航栏点击图书信息进入图书信息管理信息界面，查看现有的图书信息。图书信息表会列出图书ID、图书馆名称、类别名称、图书封面、图书名称、作者、单价、数量、当前状态、添加时间等信息，提供翻页、搜索等便利方法。

​	管理员可以点击编辑、删除、添加图书信息进行进一步管理。   

#### 7.2.14 订单管理（管理员）

​	管理员可以在导航栏点击订单管理进入订单管理信息界面，查看现有的订单信息。订单信息表会列出订单ID、图书馆名称、图书名称、图书封面、借阅状态、归还状态、订单状态、借阅时间、归还时间、借阅者姓名等信息，提供翻页、分类查找等便利方法。

​	管理员可以点击同意借阅、拒绝借阅、同意续借、拒绝续借、同意还书、拒绝还书等按钮对订单请求进行审核。 



