from django.db import models


# 客户表
class Customer(models.Model):
    id_field = models.AutoField(db_column='id_', primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    credit = models.IntegerField()
    sex = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


# 管理员表
class Manager(models.Model):
    id_field = models.IntegerField(db_column='id_', primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'manager'


# 书籍表，与数据库交互
class Book(models.Model):
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    des = models.CharField(max_length=2048, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    type_field = models.CharField(db_column='type_', max_length=255, blank=True, null=True)
    number_field = models.IntegerField(db_column='number_', blank=True, null=True)
    on_sale = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'


# 修正书籍表，与用户交互
class AmBook:
    def __init__(self, book):
        self.isbn = book.isbn
        self.title = book.title
        self.price = book.price
        self.author = book.author
        self.des = book.des
        self.img = book.img
        self.number_field = book.number_field
        self.on_sale = book.on_sale
        self.type_field = book.type_field
        kind = BookKind.objects.get(kind_id=book.type_field)
        self.type_field = kind.kind_name


# 书籍类别表
class BookKind(models.Model):
    kind_id = models.IntegerField(primary_key=True)
    kind_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_kind'


# 销售表
class Sell(models.Model):
    id_field = models.IntegerField(db_column='id_', primary_key=True)
    isbn = models.CharField(db_column='ISBN', max_length=255, blank=True, null=True)
    customer = models.IntegerField(blank=True, null=True)
    number_field = models.IntegerField(db_column='number_', blank=True, null=True)
    price1 = models.DecimalField(max_digits=64, decimal_places=0, blank=True, null=True)
    price2 = models.DecimalField(max_digits=64, decimal_places=0, blank=True, null=True)
    address = models.CharField(max_length=2048, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sell'


# 预售表
class PreSell(models.Model):
    id_field = models.IntegerField(db_column='id_', primary_key=True)
    isbn = models.CharField(db_column='ISBN', max_length=255, blank=True, null=True)
    customer = models.IntegerField(blank=True, null=True)
    number_field = models.IntegerField(db_column='number_', blank=True, null=True)
    price1 = models.DecimalField(max_digits=64, decimal_places=0, blank=True, null=True)
    price2 = models.DecimalField(max_digits=64, decimal_places=0, blank=True, null=True)
    address = models.CharField(max_length=2048, blank=True, null=True)
    finish = models.IntegerField(blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pre_sell'


# 退货表
class Back(models.Model):
    id_field = models.IntegerField(db_column='id_', primary_key=True)
    isbn = models.CharField(db_column='ISBN', max_length=255, blank=True, null=True)
    customer = models.IntegerField(blank=True, null=True)
    number_field = models.IntegerField(db_column='number_', blank=True, null=True)
    money = models.DecimalField(max_digits=64, decimal_places=0, blank=True, null=True)
    finish = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'back'


class Pie:
    def __init__(self):
        self.value = {}
        self.total = 0


class Line:
    def __init__(self):
        self.months = []
        self.title = []
