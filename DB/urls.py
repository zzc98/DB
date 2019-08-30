from django.contrib import admin
from user import views as uv
from manager import views as mv
from django.urls import path, re_path

urlpatterns = [
    # 全局页面
    path('', uv.home),
    path('admin/', admin.site.urls),

    # 管理员相关路由

    # 1 登录
    path('manager/login', mv.login),  # 跳转至登录页面
    path('manager/valid', mv.valid),  # 进行登录验证
    path('manager/index', mv.index),  # 登录成功，页面跳转
    path('manager/quit', mv.home),  # 管理员退出

    # 2. 书籍管理
    path('manager/bookinfo', mv.bookinfo),  # 显示所有书籍
    path('manager/add_book', mv.add_book),  # 增加书籍
    path('manager/delete_book', mv.delete_book),  # 删除书籍
    path('manager/change_book_info', mv.change_book_info),  # 修改书籍
    re_path('manager/search_book/.*', mv.search_book),  # 条件查询书籍

    # 3. 书籍类别管理
    path('manager/bookkind', mv.book_kind),  # 显示所有书籍类别
    path('manager/add_kind', mv.add_kind),  # 增加书籍类别
    path('manager/delete_kind', mv.delete_kind),  # 删除书籍类别
    path('manager/change_kind', mv.change_kind),  # 修改书籍类别

    # 4. 客户管理
    path('manager/customerinfo', mv.user_info),  # 初始化用户信息
    path('manager/add_user', mv.add_user),  # 增加用户
    path('manager/delete_user', mv.delete_user),  # 删除用户
    path('manager/change_user_info', mv.change_user_info),  # 修改用户
    re_path('manager/search_user/.*', mv.search_user),  # 条件查询用户

    # 5. 销售订单管理
    path('manager/sellinfo', mv.sell_info),  # 初始化信息
    path('manager/add_sell', mv.add_sell),  # 增加订单
    path('manager/delete_sell', mv.delete_sell),  # 删除订单
    path('manager/change_sell_info', mv.change_sell_info),  # 修改订单
    re_path('manager/search_sell/.*', mv.search_sell),  # 条件查询订单

    # 6. 预售订单管理
    path('manager/pre_sellinfo', mv.pre_sell_info),  # 初始化信息
    path('manager/add_pre_sell', mv.add_pre_sell),  # 增加预售订单
    path('manager/delete_pre_sell', mv.delete_pre_sell),  # 删除预售订单
    path('manager/change_pre_sell_info', mv.change_pre_sell_info),  # 修改预售订单
    re_path('manager/search_pre_sell/.*', mv.search_pre_sell),  # 条件查询预售订单

    # 7. 退货订单管理
    path('manager/backinfo', mv.back_info),  # 初始化信息
    path('manager/add_back', mv.add_back),  # 增加退货订单
    path('manager/delete_back', mv.delete_back),  # 删除退货订单
    path('manager/change_back_info', mv.change_back_info),  # 修改退货订单
    re_path('manager/search_back/.*', mv.search_back),  # 条件查询退货订单

    # 8. 管理员账号管理
    path('manager/manager_account', mv.manager_account),  # 初始化管理员列表
    path('manager/manager_valid', mv.manager_valid),  # 管理员权限认证
    path('manager/add_manager', mv.add_manager),  # 增加管理员
    path('manager/delete_manager', mv.del_manager),  # 删除管理员
    path('manager/change_manager', mv.change_manager),  # 修改管理员信息

    # 9. 统计
    path('manager/chart1', mv.chart1),  # 销售统计
    path('manager/chart2', mv.chart2),  # 预售统计
    path('manager/chart3', mv.chart3),  # 退货统计

    # 用户相关路由

    # 1. 登录注册
    path('user/login', uv.login),  # 跳转至登录页面
    path('user/register', uv.register),  # 注册函数
    path('user/valid', uv.valid),  # 登录验证函数
    path('user/index', uv.user_index),  # 登录成功，页面跳转
    path('user/quit', uv.login),  # 用户退出

    # 2. 浏览/购书等
    path('user/getNameByID', uv.get_name_by_id),  # 得到用户名
    path('user/getCreditByID', uv.get_credit_by_id),  # 得到用户积分
    path('user/searchBookByKey', uv.search_book_by_key),  # 查询书籍
    path('user/searchBookByKind', uv.search_book_by_kind),  # 书籍分类类别
    path('user/buy_book', uv.buy_book),  # 购买事件
    re_path('user/go_buy_book.*', uv.go_buy_book),  # 跳转至购书页面

    # 3. 用户管理信息
    path('user/goto_userManage', uv.manage),  # 跳转至用户管理页面
    path('user/user_person.html', uv.personInfo),  # 框架1 大类
    path('user/user_orders.html', uv.orders),  # 框架2 大类
    path('user/getInfo', uv.info),  # 得到用户信息
    path('user/change_info', uv.change_info),  # 修改用户信息
    path('user/change_pwd', uv.change_pwd),  # 修改用户密码

    # 4. 用户管理订单
    path('user/getOrder1', uv.get_order1),  # 显示销售订单
    path('user/getOrder2', uv.get_order2),  # 显示预售订单
    path('user/getOrder3', uv.get_order3),  # 显示退货订单
    path('user/back_order1', uv.back1),  # 销售书籍退货
    path('user/back_order2', uv.back2),  # 预售书籍退货
]
