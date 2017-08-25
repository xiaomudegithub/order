# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import * 

# Register your models here.
# admin.site.register(DishMenu)
# admin.site.register(Select)
admin.site.register(User)
admin.site.register(Shop)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Company)
