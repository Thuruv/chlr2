# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0003_auto_20150821_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='addedon',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 21, 23, 34, 7, 186000)),
        ),
    ]
