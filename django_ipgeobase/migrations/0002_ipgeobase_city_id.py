# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ipgeobase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipgeobase',
            name='city_id',
            field=models.IntegerField(help_text='Внутренний Ipgeobase Id Города', null=True, verbose_name='Ipgeobase Id Города'),
        ),
    ]
