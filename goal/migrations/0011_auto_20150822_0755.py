# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0010_auto_20150822_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='quality',
            field=models.FloatField(default=0, verbose_name=b'The Qulaity'),
        ),
    ]
