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


# 书籍表
class Book(models.Model):
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    des = models.CharField(max_length=2048, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    type_field = models.IntegerField(db_column='type_', blank=True, null=True)
    number_field = models.IntegerField(db_column='number_', blank=True, null=True)
    on_sale = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'


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


# 展示销售对象
class Order1:
    def __init__(self):
        self.id_field = None
        self.isbn = None
        self.title = None
        self.img = None
        self.number_field = None
        self.price2 = None
        self.address = None
        self.phone = None
        self.time = None


# 展示预售对象
class Order2:
    def __init__(self):
        self.id_field = None
        self.isbn = None
        self.title = None
        self.img = None
        self.number_field = None
        self.price2 = None
        self.address = None
        self.phone = None
        self.finish = None
        self.time = None


# 展示退货对象
class Order3:
    def __init__(self):
        self.id_field = None
        self.isbn = None
        self.title = None
        self.img = None
        self.number_field = None
        self.finish = None
        self.time = None


# 数据类型转换
def convert_to_builtin_type(obj):
    d = {}
    d.update(obj.__dict__)
    return d
