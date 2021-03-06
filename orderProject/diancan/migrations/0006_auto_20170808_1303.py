# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-08 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diancan', '0005_auto_20170801_1144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': '\u83dc\u5355', 'verbose_name_plural': '\u83dc\u5355\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '\u8ba2\u5355', 'verbose_name_plural': '\u8ba2\u5355\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': '\u5546\u94fa', 'verbose_name_plural': '\u5546\u94fa\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237\u7ba1\u7406'},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='menuId',
            new_name='orderId',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pwd',
        ),
        migrations.AddField(
            model_name='user',
            name='companyName',
            field=models.CharField(default=0, max_length=128, verbose_name='\u516c\u53f8\u540d'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='menuName',
            field=models.CharField(max_length=64, verbose_name='\u83dc\u5355\u540d'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='shopId',
            field=models.IntegerField(verbose_name='\u5546\u94faId'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shopId',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, verbose_name='\u5546\u94faId'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userName',
            field=models.CharField(max_length=64, verbose_name='\u7528\u6237\u540d'),
        ),
    ]
