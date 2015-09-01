# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0008_report_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='quality',
            field=models.FloatField(default=0, verbose_name=b'The Qulaity'),
        ),
        migrations.AlterField(
            model_name='report',
            name='details',
            field=models.CharField(max_length=256, verbose_name=b'Any Details to Dump', blank=True),
        ),
    ]
