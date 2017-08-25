# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class DishMenu(models.Model):
    MEET = "MEET"
    HALFMEET = "HALFMEET"
    NOMEET = "NOMEET"
    DISH_TYPE_CHOICES = (
        (MEET,"荤菜"),
        (HALFMEET,"半荤"),
        (NOMEET,"素菜")
    )
    dishName = models.CharField(max_length=64)
    disType = models.CharField(max_length=16, choices=DISH_TYPE_CHOICES, default=MEET)
    isSelected = models.BooleanField(default=True)

class Select(models.Model):
    userName = models.CharField(max_length=64)
    meetId = models.IntegerField(blank=False)
    meetName = models.CharField(max_length=64)
    halfMeetId = models.IntegerField(blank=False)
    halfMeetName = models.CharField(max_length=64)
    noMeetId = models.IntegerField(blank=False)
    noMeetName = models.CharField(max_length=64)
    orderTime = models.DateTimeField(auto_now=True)


class Order(models.Model):
    
    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单管理"

    def __unicode__(self):
        return self.orderTime

    orderId = models.IntegerField(blank=False)
    uid = models.IntegerField(blank=False)
    orderTime = models.DateTimeField(auto_now=True)


class Shop(models.Model):

    class Meta:
        verbose_name = u"商铺"
        verbose_name_plural = u"商铺管理"

    def __unicode__(self):
        return self.shopName

    shopId = models.IntegerField(primary_key=True, default=1, verbose_name=u'商铺Id')
    shopName = models.CharField(max_length=64, verbose_name=u'商铺名')

class Menu(models.Model):

    class Meta:
        verbose_name = "菜单"
        verbose_name_plural = "菜单管理"

    def __unicode__(self):
        return self.menuName

    menuName = models.CharField(max_length=64, verbose_name=u"菜单名")
    shopId = models.IntegerField(blank=False, verbose_name="商铺Id")


class User(models.Model):
    
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户管理"
    
    def __unicode__(self):
        return self.userName

    userName = models.CharField(max_length=64, verbose_name=u"用户名")
    companyName = models.CharField(max_length=128, verbose_name=u"公司名")

class Company(models.Model):

    class Meta:
        verbose_name = "公司"
        verbose_name_plural = "公司管理"

    def __unicode__(self):
        return ""

    companyId = models.IntegerField(default=0, verbose_name=u"公司ID")
    companyName = models.CharField(max_length=128, verbose_name=u'公司名')

