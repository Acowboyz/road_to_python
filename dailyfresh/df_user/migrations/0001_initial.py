# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('uemail', models.CharField(max_length=30)),
                ('ureciever', models.CharField(max_length=20)),
                ('uaddress', models.CharField(max_length=100)),
                ('upostcode', models.CharField(max_length=6)),
                ('uphone', models.CharField(max_length=11)),
            ],
        ),
    ]
