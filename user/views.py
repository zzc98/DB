from django.shortcuts import render
from user import models
from django.http import HttpResponse
import json as js
import math
import time


# Web入口页面
def home(request):
    return render(request, 'index.html')


# 跳转至用户登录界面
def login(request):
    return render(request, 'login.html')


# 进行用户登录验证
def valid(request):
    if request.method == "POST":
        id_ = request.POST["id"]
        password = request.POST["password"]
        try:
            person = models.Customer.objects.get(id_field=id_, password=password)
            return HttpResponse(js.dumps({"status": 1, "name": person.name, 'id': person.id_field}))
        except:
            return HttpResponse(js.dumps({"status": 0}))
    return HttpResponse(js.dumps({"status": 0}))


# 跳转至用户选书界面
def user_index(request):
    book_list = models.Book.objects.all()
    kind_list = models.BookKind.objects.all()
    return render(request, 'user.html', {'book_list': book_list, 'kind_list': kind_list})


# 跳转至书籍详细信息界面
def go_buy_book(request):
    isbn = request.GET['isbn']
    try:
        book = models.Book.objects.get(isbn=isbn)
        kind_list = models.BookKind.objects.all()
        return render(request, 'user_buy.html', {'book': book, 'kind_list': kind_list})
    except:
        return render(request, 'error.html')


# 购买操作
def buy_book(request):
    try:
        isbn = request.POST['isbn']
        customer = request.POST['customer']
        number_ = request.POST['number']
        if int(number_) < 0:
            return HttpResponse(js.dumps({"status": 0}))
        price1 = request.POST['price1']
        price2 = request.POST['price2']
        address = request.POST['address']
        phone = request.POST['phone']
        status = request.POST['status']
        # 创建订单 + 修改积分 + 书籍数目修改
        # 销售 number（剩余量） 减去数目，预售 number （待售量）加上数目
        book = models.Book.objects.filter(isbn=isbn)
        if int(status) == 1:  # 销售中的
            if book.first().number_field - int(number_) < 0:
                return HttpResponse(js.dumps({"status": 0}))
            try:
                all_sell = models.Sell.objects.order_by('-id_field').first()
                id_ = all_sell.id_field + 1
            except:
                id_ = 10001
            models.Sell.objects.create(id_field=id_, isbn=isbn, customer=customer, number_field=number_, price1=price1,
                                       price2=price2, address=address, phone=phone, state=1,
                                       create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            book.update(number_field=book.first().number_field - int(number_))
        else:
            try:
                all_sell = models.PreSell.objects.order_by('-id_field').first()
                id_ = all_sell.id_field + 1
            except:
                id_ = 10001
            models.PreSell.objects.create(id_field=id_, isbn=isbn, customer=customer, number_field=number_,
                                          price1=price1, price2=price2, address=address, phone=phone, state=1,
                                          create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            book.update(number_field=book.first().number_field + int(number_))
        total = math.floor(float(price1) - (float(price1) - float(price2)) * 10)
        user = models.Customer.objects.filter(id_field=customer)
        u = user.first()
        user.update(credit=u.credit + total)
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 销售书籍退货
def back1(request):
    sell_id = request.POST['sell_id']
    try:
        sell = models.Sell.objects.filter(id_field=sell_id).first()
        if sell:
            isbn = sell.isbn
            customer = sell.customer
            number_ = sell.number_field
            money = sell.price2
            try:
                all_back = models.Back.objects.order_by('-id_field').first()
                id_ = all_back.id_field + 1
            except:
                id_ = 10001
            models.Back.objects.create(id_field=id_, isbn=isbn, customer=customer, number_field=number_, money=money,
                                       finish=0, create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            sell.delete()
            return HttpResponse(js.dumps({"status": 1}))
        else:
            return HttpResponse(js.dumps({"status": 0}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 预售书籍退货
def back2(request):
    pre_sell_id = request.POST['pre_sell_id']
    try:
        pre_sell = models.PreSell.objects.filter(id_field=pre_sell_id).first()
        if pre_sell:
            isbn = pre_sell.isbn
            customer = pre_sell.customer
            number_ = pre_sell.number_field
            money = pre_sell.price2
            try:
                all_back = models.Back.objects.order_by('-id_field').first()
                id_ = all_back.id_field + 1
            except:
                id_ = 10001
            models.Back.objects.create(id_field=id_, isbn=isbn, customer=customer, number_field=number_, money=money,
                                       finish=0, create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            pre_sell.delete()
            return HttpResponse(js.dumps({"status": 1}))
        else:
            return HttpResponse(js.dumps({"status": 0}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 个人信息修改操作
def change_info(request):
    try:
        id_ = request.POST['id']
        name = request.POST['name']
        phone = request.POST['phone']
        birthday = request.POST['birthday']
        address = request.POST['address']
        sex = request.POST['sex']
        person = models.Customer.objects.filter(id_field=id_)
        person.update(name=name, phone=phone, birthday=birthday, address=address, sex=sex)
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 密码修改操作
def change_pwd(request):
    try:
        id_ = request.POST['id']
        password = request.POST['password']
        person = models.Customer.objects.filter(id_field=id_)
        person.update(password=password)
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 注册操作
def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        sex = request.POST["sex"]
        birthday = request.POST["birthday"]
        try:
            all_user = models.Customer.objects.order_by('-id_field').first()
            uid = all_user.id_field + 1
        except:
            uid = 10001
        models.Customer.objects.create(id_field=uid, name=name, password=password, phone=phone, credit=0,
                                       address=address, sex=sex, birthday=birthday)
        return HttpResponse(js.dumps({"status": 1, 'id': uid}))
    else:
        return HttpResponse(js.dumps({"status": 0}))


# 跳转至用户信息及订单界面
def manage(request):
    return render(request, 'user_manage.html')


# 跳转至用户信息界面
def personInfo(request):
    return render(request, 'user_person.html')


# 获得用户信息
def info(request):
    id_ = request.POST['id']
    try:
        person = models.Customer.objects.get(id_field=id_)
        return HttpResponse(
            js.dumps({"status": 1, 'name': person.name, 'credit': person.credit, 'phone': person.phone,
                      'gender': person.sex, 'birthday': str(person.birthday), 'address': person.address,
                      'password': person.password}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


def orders(request):
    return render(request, 'user_orders.html')


# 销售订单表
def get_order1(request):
    try:
        id_ = request.POST['id']
        sell_all = models.Sell.objects.filter(customer=id_)
        sell_all = list(sell_all)
        sell_list = list()
        for i in sell_all:
            try:
                temp = models.Order1()
                temp.id_field = i.id_field
                temp.isbn = i.isbn
                temp.title = models.Book.objects.filter(isbn=temp.isbn).first().title
                temp.img = models.Book.objects.filter(isbn=temp.isbn).first().img
                temp.number_field = i.number_field
                temp.price2 = str(i.price2)
                temp.address = i.address
                temp.phone = i.phone
                temp.time = str(i.create_time)
                temp.state = int(i.state)
                sell_list.append(models.convert_to_builtin_type(temp))
            except:
                continue
        return HttpResponse(js.dumps({"status": 1, 'list': sell_list}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 预售订单表
def get_order2(request):
    try:
        id_ = request.POST['id']
        pre_sell_all = models.PreSell.objects.filter(customer=id_)
        pre_sell_all = list(pre_sell_all)
        pre_sell_list = list()
        for i in pre_sell_all:
            try:
                temp = models.Order2()
                temp.id_field = i.id_field
                temp.isbn = i.isbn
                temp.title = models.Book.objects.filter(isbn=temp.isbn).first().title
                temp.img = models.Book.objects.filter(isbn=temp.isbn).first().img
                temp.number_field = i.number_field
                temp.price2 = str(i.price2)
                temp.address = i.address
                temp.phone = i.phone
                temp.time = str(i.create_time)
                temp.state = int(i.state)
                pre_sell_list.append(models.convert_to_builtin_type(temp))
            except:
                continue
        return HttpResponse(js.dumps({"status": 1, 'list': pre_sell_list}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 退货订单表
def get_order3(request):
    try:
        id_ = request.POST['id']
        back_all = models.Back.objects.filter(customer=id_)
        back_all = list(back_all)
        back_list = list()
        for i in back_all:
            temp = models.Order3()
            temp.id_field = i.id_field
            temp.isbn = i.isbn
            temp.title = models.Book.objects.filter(isbn=temp.isbn).first().title
            temp.img = models.Book.objects.filter(isbn=temp.isbn).first().img
            temp.number_field = i.number_field
            temp.finish = i.finish
            temp.time = str(i.create_time)
            back_list.append(models.convert_to_builtin_type(temp))
        return HttpResponse(js.dumps({"status": 1, 'list': back_list}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 通过关键词查询书籍
def search_book_by_key(request):
    key = request.GET['key']
    kind_list = models.BookKind.objects.all()
    book_list = models.Book.objects.all()
    book_list = models.Book.objects.filter(isbn=key) | book_list.filter(title__contains=key) | book_list.filter(
        author__contains=key) | book_list.filter(des__contains=key)
    return render(request, 'user.html', {'book_list': book_list, 'kind_list': kind_list})


# 通过类别查询书籍
def search_book_by_kind(request):
    kind = request.GET['kind']
    kind_list = models.BookKind.objects.all()
    book_list = models.Book.objects.all()
    book_list = book_list.filter(type_field=kind)
    return render(request, 'user.html', {'book_list': book_list, 'kind_list': kind_list})


# 通过ID得到用户名
def get_name_by_id(request):
    id_ = request.POST['id']
    try:
        person = models.Customer.objects.get(id_field=id_)
        return HttpResponse(js.dumps({"status": 1, 'name': person.name}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 通过ID得到积分
def get_credit_by_id(request):
    id_ = request.POST['id']
    try:
        person = models.Customer.objects.get(id_field=id_)
        return HttpResponse(js.dumps({"status": 1, 'credit': person.credit}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 销售订单确认收货
def confirm1(request):
    sell_id = request.POST['sell_id']
    try:
        sell = models.Sell.objects.filter(id_field=sell_id)
        sell.update(state=3)  # 状态值由2变为3
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 预售订单确认收货
def confirm2(request):
    pre_sell_id = request.POST['pre_sell_id']
    try:
        pre_sell = models.PreSell.objects.filter(id_field=pre_sell_id)
        pre_sell.update(state=3)  # 状态值由2变为3
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))
