# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0011_auto_20150822_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateField(default=b'08/26/2015', verbose_name=b'Report Date'),
        ),
        migrations.AlterField(
            model_name='report',
            name='worker',
            field=models.CharField(max_length=25, verbose_name=b'Whois it?', choices=[(b'Thiliban', b'Thiliban'), (b'Ramachandran', b'Ramachandran'), (b'Sathish', b'Sathish'), (b'Pradeep Anand', b'Pradeep Anand'), (b'Prathipa', b'Prathipa'), (b'Madhan', b'Madhan'), (b'Gayathri', b'Gayathri'), (b'Karthick', b'Karthick'), (b'Aqhil Mohammad', b'Aqhil Mohammad'), (b'Soniya', b'Soniya'), (b'Aamir Khan', b'Aamir Khan')]),
        ),
    ]
