# coding=utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FileInfo(models.Model):
    class Meta:
        db_table = 'food_file_info'
    filename = models.CharField(max_length=200)
    filepath = models.CharField(max_length=200,unique=True)
    filesize = models.IntegerField(default=0,null=True)
    filetype = models.CharField(max_length=30,null=True)
    user = models.ForeignKey(User)
    createtime = models.IntegerField(null=True)

'''店铺'''

class ShopInfo(models.Model):
    class Meta:
        db_table = 'food_shop'
    shop_name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='chirldren') #连锁店
    shop_type = models.IntegerField(null=True)
    tag = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    master = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    domain =  models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.CharField(max_length=50, null=True, blank=True)  # 经度
    longitude = models.CharField(max_length=50, null=True, blank=True)  # 纬度
    manager_counts = models.IntegerField(default=1)
    status = models.IntegerField(default=0, null=True)
    business = models.CharField(max_length=200, null=True)
    wechat = models.CharField(max_length=40, null=True)  # 微信
    identify = models.CharField(max_length=20, null=True)  # 身份证
    photo = models.CharField(max_length=100, null=True)  # 头像
    validation = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    createtime = models.IntegerField(null=True)

'''店铺管理员'''

class ShopManager(models.Model):
    class Meta:
        db_table = 'food_shop_manager'
    shop = models.ForeignKey(ShopInfo)
    user = models.ForeignKey(User)
    is_active = models.BooleanField(default=True)

'''食品类型'''

class FoodType(models.Model):
    class Meta:
        db_table = 'food_food_type'
    type_name = models.CharField(max_length=20)

'''食品味道'''

class FoodDelicious(models.Model):
    class Meta:
        db_table = 'food_food_delicious'
    delicious_name = models.CharField(max_length=20)
    image_icon = models.CharField(max_length=20,null=True)

'''食品信息'''

class FoodInfo(models.Model):
    class Meta:
        db_table = 'food_food_info'
    food_name = models.CharField(max_length=50)
    food_type = models.ForeignKey(FoodType,default=0,null=True) # 类型
    shop = models.ForeignKey(ShopInfo)
    description = models.CharField(max_length=200,null=True)
    photo = models.ManyToManyField(FileInfo,null=True)
    materials = models.CharField(max_length=200,null=True) # 原料
    price = models.FloatField(default=0, null=True) # 价格
    discount = models.FloatField(default=0, null=True) # 优惠
    make_time = models.IntegerField(default=0,null=True)
    delicious_type = models.ForeignKey(FoodDelicious,default=0,null=True) # 味道类型[辣]
    total_counts = models.IntegerField(default=-1,null=True) # 数量
    is_active = models.BooleanField(default=True)
    createtime = models.IntegerField(null=True)

'''个人信息'''

class UserProfile(models.Model):
    class Meta:
        db_table = 'food_user_profile'

    user = models.ForeignKey(User, unique=True)
    sex = models.IntegerField(default=0, null=True)
    birthday = models.CharField(max_length=20,null=True)
    phone = models.CharField(max_length=20, null=True)
    mobile = models.CharField(max_length=20, null=True)
    qq = models.CharField(max_length=20, null=True)
    wechat = models.CharField(max_length=40, null=True)  # 微信
    photo = models.CharField(max_length=100, null=True)  # 头像
    province = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=20, null=True)
    area = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=50, null=True)
    occupational_type = models.IntegerField(default=0, null=True) # 职业类型
    remark = models.CharField(max_length=50, null=True) # 一句话描述
    validatecode = models.CharField(max_length=50, null=True)  # 邀请码
    isvalidated = models.BooleanField(default=False)  # 是否激活


class MicroTopic(models.Model):
    class Meta:
        db_table = 'food_micro_topic'
    topic_name = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    createtime = models.IntegerField(null=True)


class Microblog(models.Model):
    class Meta:
        db_table = 'food_micro_blog'

    content = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    topic = models.ForeignKey(MicroTopic,null=True)
    source = models.CharField(max_length=200,null=True)
    createtime = models.IntegerField(null=True)
