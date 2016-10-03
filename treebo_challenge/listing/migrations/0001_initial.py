# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel_Deals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=500, null=True, blank=True)),
                ('image', models.CharField(max_length=500, null=True, blank=True)),
                ('rating', models.FloatField(max_length=10, null=True, blank=True)),
                ('link', models.CharField(max_length=500, null=True, blank=True)),
                ('actual_price', models.CharField(max_length=100000, null=True, blank=True)),
                ('discount', models.CharField(max_length=1000, null=True, blank=True)),
                ('location', models.CharField(max_length=1000, null=True, blank=True)),
            ],
        ),
    ]
