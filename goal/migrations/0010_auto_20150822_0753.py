# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0009_auto_20150822_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='quality',
            field=models.FloatField(default=b'error*count', verbose_name=b'The Qulaity'),
        ),
    ]
