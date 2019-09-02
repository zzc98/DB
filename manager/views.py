from django.shortcuts import render
import json as js
from manager import models
from django.http import HttpResponse
import time
import base64
import face_recognition


def home(request):
    return render(request, 'index.html')


# 跳转至管理员登录界面
def login(request):
    return render(request, 'login_manager.html')


# 进行管理员登录验证
def valid(request):
    m_id = request.POST["id"]
    password = request.POST["password"]
    try:
        models.Manager.objects.get(id_field=m_id, password=password)
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 跳转至管理员界面
def index(request):
    return render(request, 'manager.html')


# 书籍信息查询
def bookinfo(request):
    book_list = models.Book.objects.all()
    b = []
    for i in book_list:
        b.append(models.AmBook(i))
    book_list = b
    kinds = models.BookKind.objects.all()
    return render(request, 'frame1.html', {'book_list': book_list, 'kind_list': kinds})


# 修改书籍信息
def change_book_info(request):
    try:
        isbn = request.POST['isbn']
        title = request.POST["title"]
        price = request.POST["price"]
        author = request.POST["author"]
        des = request.POST["des"]
        type_ = request.POST["type"]
        number_ = request.POST["number"]
        if int(number_) < 0:
            return HttpResponse(js.dumps({"status": 0}))
        on_sale = request.POST["on_sale"]
        book = models.Book.objects.filter(isbn=isbn)
        book.update(title=title, price=price, author=author, des=des, type_field=type_,
                    number_field=number_, on_sale=on_sale)
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 删除书籍
def delete_book(request):
    try:
        book = models.Book.objects.get(isbn=request.POST["isbn"])
        book.delete()
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 增加书籍
def add_book(request):
    try:
        isbn = request.POST.get('isbn')
        title = request.POST.get("title")
        price = request.POST.get("price")
        author = request.POST.get("author")
        des = request.POST.get("des")
        type_ = request.POST.get("type")
        number_ = request.POST.get("number")
        on_sale = request.POST.get("on_sale")
        book = models.Book.objects.filter(isbn=isbn)
        if book:
            return HttpResponse(js.dumps({"status": 0}))
        obj = request.FILES.get('img')
        f_obj = open('static/book_img/' + obj.name, 'wb+')
        for chunk in obj.chunks():
            f_obj.write(chunk)
        f_obj.close()
        full_path = '/static/book_img/%s' % obj.name
        models.Book.objects.create(isbn=isbn, title=title, price=price, author=author, des=des, type_field=type_,
                                   number_field=number_, img=full_path, on_sale=on_sale)
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 书籍条件查询
def search_book(request):
    book_list = models.Book.objects.all()
    kinds = models.BookKind.objects.all()
    try:
        a = request.GET['a']
        if a:
            book_list = book_list.filter(isbn=a)
        b = request.GET['b']
        if b:
            book_list = book_list.filter(title__contains=b)
        c = request.GET['c']
        if c:
            book_list = book_list.filter(author__contains=c)
        d = request.GET['d']
        if d:
            book_list = book_list.filter(type_field=d)
        e = request.GET['e']
        if e:
            book_list = book_list.filter(on_sale=e)
        b = []
        for i in book_list:
            b.append(models.AmBook(i))
        book_list = b
        return render(request, 'frame1.html', {'book_list': book_list, 'kind_list': kinds})
    except:
        return render(request, 'frame1.html', {'book_list': book_list, 'kind_list': kinds})


# 书籍类别查询
def book_kind(request):
    kind_list = models.BookKind.objects.all()
    return render(request, 'frame1_1.html', {'kind_list': kind_list})


# 增加类别
def add_kind(request):
    try:
        kind_name = request.POST.get('kind_name')
        kind = models.BookKind.objects.filter(kind_name=kind_name)
        if kind:
            return HttpResponse(js.dumps({"status": 0}))
        try:
            all_kind = models.BookKind.objects.order_by("-kind_id").first()
            kid = all_kind.kind_id + 1
        except:
            kid = 1
        models.BookKind.objects.create(kind_id=kid, kind_name=kind_name)
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 删除类别
def delete_kind(request):
    try:
        kid = request.POST["kind_id"]
        kind = models.BookKind.objects.filter(kind_id=kid)
        if kind:
            kind.delete()
            return HttpResponse(js.dumps({"status": 1}))
        else:
            return HttpResponse(js.dumps({"status": 0}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 修改类别
def change_kind(request):
    try:
        kid = request.POST["kind_id"]
        kname = request.POST["kind_name"]
        kind = models.BookKind.objects.filter(kind_id=kid)
        kind.update(kind_name=kname)
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 初始化客户信息
def user_info(request):
    user_list = models.Customer.objects.all()
    return render(request, 'frame2.html', {'user_list': user_list})


# 修改客户信息
def change_user_info(request):
    try:
        uid = request.POST["uid"]
        name = request.POST["name"]
        password = request.POST["password"]
        phone = request.POST["phone"]
        credit = request.POST["credit"]
        sex = request.POST["sex"]
        birthday = request.POST["birthday"]
        address = request.POST["address"]
        user = models.Customer.objects.filter(id_field=uid)
        user.update(name=name, password=password, phone=phone, credit=credit, sex=sex,
                    birthday=birthday, address=address)
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 注销客户信息
def delete_user(request):
    try:
        uid = request.POST["uid"]
        user = models.Customer.objects.filter(id_field=uid)
        if user:
            user.delete()
            return HttpResponse(js.dumps({"status": 1}))
        else:
            return HttpResponse(js.dumps({"status": 0}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 增加客户
def add_user(request):
    try:
        name = request.POST["name"]
        password = request.POST["password"]
        phone = request.POST["phone"]
        credit = request.POST["credit"]
        sex = request.POST["sex"]
        birthday = request.POST["birthday"]
        address = request.POST["address"]
        check = models.Customer.objects.fliter(phone=phone)
        if check.count() == 0:
            return HttpResponse(js.dumps({"status": 2}))
        try:
            all_user = models.Customer.objects.order_by('-id_field').first()
            uid = all_user.id_field + 1
        except:
            uid = 10001
        models.Customer.objects.create(id_field=uid, name=name, password=password, phone=phone, credit=credit, sex=sex,
                                       birthday=birthday, address=address)
        return HttpResponse(js.dumps({"status": 1, 'uid': uid}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 客户条件查询
def search_user(request):
    user_list = models.Customer.objects.all()
    try:
        a = request.GET['a']
        if a:
            user_list = user_list.filter(id_field=a)
        b = request.GET['b']
        if b:
            user_list = user_list.filter(name__contains=b)
        return render(request, 'frame2.html', {'user_list': user_list})
    except:
        return render(request, 'frame2.html', {'user_list': user_list})


# 初始销售信息
def sell_info(request):
    sell_list = models.Sell.objects.all()
    return render(request, 'frame3.html', {'sell_list': sell_list})


# 修改销售信息
def change_sell_info(request):
    try:
        id_ = request.POST["id"]
        isbn = request.POST['isbn']
        customer = request.POST['customer']
        number_ = request.POST['number']
        price1 = request.POST['price1']
        price2 = request.POST['price2']
        address = request.POST['address']
        phone = request.POST['phone']
        state = request.POST['state']
        sell = models.Sell.objects.filter(id_field=id_)
        sell.update(isbn=isbn, customer=customer, number_field=number_, price1=price1, price2=price2, address=address,
                    phone=phone, state=state)
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 注销销售信息
def delete_sell(request):
    try:
        id_ = request.POST["id"]
        sell = models.Sell.objects.filter(id_field=id_)
        if sell:
            sell.delete()
            return HttpResponse(js.dumps({"status": 1}))
        else:
            return HttpResponse(js.dumps({"status": 0}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 增加销售
def add_sell(request):
    try:
        isbn = request.POST['isbn']
        customer = request.POST['customer']
        # 检查是否有此书籍、顾客
        models.Book.objects.get(isbn=isbn)
        models.Customer.objects.get(id_field=customer)
        number_ = request.POST['number']
        price1 = request.POST['price1']
        price2 = request.POST['price2']
        address = request.POST['address']
        phone = request.POST['phone']
        state = request.POST['state']
        try:
            all_sell = models.Sell.objects.order_by('-id_field').first()
            id_ = all_sell.id_field + 1
        except:
            id_ = 10001
        models.Sell.objects.create(id_field=id_, isbn=isbn, customer=customer, number_field=number_, price1=price1,
                                   price2=price2, address=address, phone=phone, state=state,
                                   create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return HttpResponse(js.dumps({"status": 1, 'id': id_}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 销售条件查询
def search_sell(request):
    sell_list = models.Sell.objects.all()
    try:
        a = request.GET['a']
        if a:
            sell_list = sell_list.filter(id_field=a)
        b = request.GET['b']
        if b:
            sell_list = sell_list.filter(isbn=b)
        c = request.GET['c']
        if c:
            sell_list = sell_list.filter(customer__contains=c)
        return render(request, 'frame3.html', {'sell_list': sell_list})
    except:
        return render(request, 'frame3.html', {'sell_list': sell_list})


# 初始预售信息
def pre_sell_info(request):
    pre_sell_list = models.PreSell.objects.all()
    return render(request, 'frame4.html', {'pre_sell_list': pre_sell_list})


# 修改预售信息
def change_pre_sell_info(request):
    try:
        id_ = request.POST["id"]
        isbn = request.POST['isbn']
        customer = request.POST['customer']
        number_ = request.POST['number']
        price1 = request.POST['price1']
        price2 = request.POST['price2']
        address = request.POST['address']
        phone = request.POST['phone']
        state = request.POST['state']
        pre_sell = models.PreSell.objects.filter(id_field=id_)
        pre_sell.update(isbn=isbn, customer=customer, number_field=number_, price1=price1, price2=price2,
                        address=address, phone=phone, state=state)
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 注销预售信息
def delete_pre_sell(request):
    try:
        id_ = request.POST["id"]
        pre_sell = models.PreSell.objects.filter(id_field=id_)
        if pre_sell:
            pre_sell.delete()
            return HttpResponse(js.dumps({"status": 1}))
        else:
            return HttpResponse(js.dumps({"status": 0}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 增加预售
def add_pre_sell(request):
    try:
        isbn = request.POST['isbn']
        customer = request.POST['customer']
        # 检查是否有此书籍、顾客
        models.Book.objects.get(isbn=isbn)
        models.Customer.objects.get(id_field=customer)
        number_ = request.POST['number']
        price1 = request.POST['price1']
        price2 = request.POST['price2']
        address = request.POST['address']
        phone = request.POST['phone']
        state = request.POST['state']
        try:
            all_sell = models.PreSell.objects.order_by('-id_field').first()
            id_ = all_sell.id_field + 1
        except:
            id_ = 10001
        models.PreSell.objects.create(id_field=id_, isbn=isbn, customer=customer, number_field=number_, price1=price1,
                                      price2=price2, address=address, phone=phone, state=state,
                                      create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return HttpResponse(js.dumps({"status": 1, 'id': id_}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 预售条件查询
def search_pre_sell(request):
    pre_sell_list = models.PreSell.objects.all()
    try:
        a = request.GET['a']
        if a:
            pre_sell_list = pre_sell_list.filter(id_field=a)
        b = request.GET['b']
        if b:
            pre_sell_list = pre_sell_list.filter(isbn=b)
        c = request.GET['c']
        if c:
            pre_sell_list = pre_sell_list.filter(customer__contains=c)
        return render(request, 'frame4.html', {'pre_sell_list': pre_sell_list})
    except:
        return render(request, 'frame4.html', {'pre_sell_list': pre_sell_list})


# 初始退货信息
def back_info(request):
    back_list = models.Back.objects.all()
    return render(request, 'frame5.html', {'back_list': back_list})


# 修改退货信息
def change_back_info(request):
    try:
        id_ = request.POST["id"]
        isbn = request.POST['isbn']
        customer = request.POST['customer']
        number_ = request.POST['number']
        money = request.POST['money']
        finish = request.POST['finish']
        back = models.Back.objects.filter(id_field=id_)
        back.update(isbn=isbn, customer=customer, number_field=number_, money=money, finish=finish)
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 注销退货信息
def delete_back(request):
    try:
        id_ = request.POST["id"]
        back = models.Back.objects.filter(id_field=id_)
        if back:
            back.delete()
            return HttpResponse(js.dumps({"status": 1}))
        else:
            return HttpResponse(js.dumps({"status": 0}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 增加退货
def add_back(request):
    try:
        isbn = request.POST['isbn']
        customer = request.POST['customer']
        # 检查是否有此书籍、顾客
        models.Book.objects.get(isbn=isbn)
        models.Customer.objects.get(id_field=customer)
        number_ = request.POST['number']
        money = request.POST['money']
        finish = request.POST['finish']
        try:
            all_back = models.Back.objects.order_by('-id_field').first()
            id_ = all_back.id_field + 1
        except:
            id_ = 10001
        models.Back.objects.create(id_field=id_, isbn=isbn, customer=customer, number_field=number_, money=money,
                                   finish=finish, create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return HttpResponse(js.dumps({"status": 1, 'id': id_}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 退货条件查询
def search_back(request):
    back_list = models.Back.objects.all()
    try:
        a = request.GET['a']
        if a:
            back_list = back_list.filter(id_field=a)
        b = request.GET['b']
        if b:
            back_list = back_list.filter(isbn=b)
        c = request.GET['c']
        if c:
            back_list = back_list.filter(customer__contains=c)
        d = request.GET['d']
        if d:
            back_list = back_list.filter(finish=d)
        return render(request, 'frame5.html', {'back_list': back_list})
    except:
        return render(request, 'frame5.html', {'back_list': back_list})


# 销售统计
def chart1(request):
    pie = models.Pie()
    line = models.Line()
    chart_count(1, pie, line)
    return render(request, 'frame6.html', {'pie': pie, 'line': line})


# 预售统计
def chart2(request):
    pie = models.Pie()
    line = models.Line()
    chart_count(2, pie, line)
    return render(request, 'frame6.html', {'pie': pie, 'line': line})


# 退货统计
def chart3(request):
    pie = models.Pie()
    line = models.Line()
    chart_count(3, pie, line)
    return render(request, 'frame6.html', {'pie': pie, 'line': line})


# 销量统计
def chart_count(chart_type, pie, line):
    if chart_type == 1:
        objs = models.Sell.objects
    elif chart_type == 2:
        objs = models.PreSell.objects
    else:
        objs = models.Back.objects
    year = int(time.strftime("%Y", time.localtime()))
    month = int(time.strftime("%m", time.localtime()))
    samples = objs.filter(create_time__year=year, create_time__month=month)  # 数据缓冲池
    kind_list = models.BookKind.objects.all()
    for i in kind_list:
        pie.value[i.kind_name] = 0
    for i in samples:
        book = models.Book.objects.get(isbn=i.isbn)
        try:
            money = float(i.price2)
        except:
            money = float(i.money)
        pie.value[kind_list.get(kind_id=book.type_field).kind_name] += money
        pie.total += money
    temp_year = year - 1
    if month == 1:
        months_list = [9, 10, 11, 12, 1]
        years_list = [temp_year, temp_year, temp_year, temp_year, year]
    elif month == 2:
        months_list = [10, 11, 12, 1, 2]
        years_list = [temp_year, temp_year, temp_year, year, year]
    elif month == 3:
        months_list = [11, 12, 1, 2, 3]
        years_list = [temp_year, temp_year, year, year, year]
    elif month == 4:
        months_list = [12, 1, 2, 3, 4]
        years_list = [temp_year, year, year, year, year]
    else:
        months_list = [month - 4, month - 3, month - 2, month - 1, month]
        years_list = [year, year, year, year, year]
    for i in range(5):
        line.title.append("{}-{}".format(years_list[i], months_list[i]))  # 记录时间标题
        samples = objs.filter(create_time__year=years_list[i], create_time__month=months_list[i])
        temp_dict = {}
        for j in kind_list:
            temp_dict[j.kind_name] = 0
        for j in samples:
            book = models.Book.objects.get(isbn=j.isbn)
            try:
                money = float(j.price2)
            except:
                money = float(j.money)
            temp_dict[kind_list.get(kind_id=book.type_field).kind_name] += money
        line.months.append(temp_dict)


# 管理员信息管理
def manager_account(request):
    manager_list = models.Manager.objects.all()
    return render(request, 'frame2_1.html', {'manager_list': manager_list})


# 增加管理员
def add_manager(request):
    try:
        manager_name = request.POST['manager_name']
        manager_password = request.POST['manager_password']
        all_manager = models.Manager.objects.order_by("-id_field").first()
        mid = all_manager.id_field + 1
        models.Manager.objects.create(id_field=mid, name=manager_name, password=manager_password)
        return HttpResponse(js.dumps({"status": 1, "mid": mid}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 删除管理员
def del_manager(request):
    try:
        manager_id = request.POST['manager_id']
        manager = models.Manager.objects.get(id_field=manager_id)
        manager.delete()
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 修改管理员
def change_manager(request):
    try:
        manager_id = request.POST['manager_id']
        manager_name = request.POST['manager_name']
        manager_password = request.POST['manager_password']
        manager = models.Manager.objects.filter(id_field=manager_id)
        manager.update(name=manager_name, password=manager_password)
        return HttpResponse(js.dumps({"status": 1}))
    except:
        return HttpResponse(js.dumps({"status": 0}))


# 管理员身份认证
def manager_valid(request):
    try:
        data = request.POST["image"]
        i1 = data.split('base64,')
        img_data = base64.b64decode(i1[1])
        with open('static/manager_account/temp.jpg', 'wb') as f:
            f.write(img_data)
        img1 = face_recognition.load_image_file("static/manager_account/manager.jpg")
        data1 = face_recognition.face_encodings(img1)[0]
        img2 = face_recognition.load_image_file("static/manager_account/temp.jpg")
        data2 = face_recognition.face_encodings(img2)[0]
        res = face_recognition.compare_faces([data1], data2)
        if res[0]:
            return HttpResponse(js.dumps({"status": 1}))
        else:
            return HttpResponse(js.dumps({"status": 0}))
    except:
        return HttpResponse(js.dumps({"status": 0}))
