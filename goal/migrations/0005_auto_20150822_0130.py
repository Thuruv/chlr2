# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0004_report_addedon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='addedon',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateField(default=b'08/22/2015', verbose_name=b'Report Date'),
        ),
    ]
