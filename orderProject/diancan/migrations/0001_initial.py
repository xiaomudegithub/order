# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-03 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DishMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishName', models.CharField(max_length=64)),
                ('disType', models.CharField(choices=[('MEET', '\u8364\u83dc'), ('HALFMEET', '\u534a\u8364'), ('NOMEET', '\u7d20\u83dc')], default='MEET', max_length=16)),
                ('isSelected', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Select',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('userName', models.CharField(max_length=64)),
                ('meetId', models.IntegerField()),
                ('meetName', models.CharField(max_length=64)),
                ('halfMeetId', models.IntegerField()),
                ('halfMeetName', models.CharField(max_length=64)),
                ('noMeetId', models.IntegerField()),
                ('noMeetName', models.CharField(max_length=64)),
                ('orderTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=64)),
                ('pwd', models.CharField(max_length=128)),
            ],
        ),
    ]
