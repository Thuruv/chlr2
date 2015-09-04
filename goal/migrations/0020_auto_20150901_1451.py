# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0019_auto_20150901_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='worker',
            field=models.CharField(default=b'Select Something', max_length=25, verbose_name=b'Whois it?', choices=[(b'Venkat', b'Venkat'), (b'Select Something', b'Select Something'), (b'Thiliban', b'Thiliban'), (b'Ramachandran', b'Ramachandran'), (b'Sathish', b'Sathish'), (b'Pradeep Anand', b'Pradeep Anand'), (b'Prathiba', b'Prathiba'), (b'Madhan', b'Madhan'), (b'Gayathri', b'Gayathri'), (b'Karthick', b'Karthick'), (b'Aqhil Mohammad', b'Aqhil Mohammad'), (b'Soniya', b'Soniya'), (b'Aamir Khan', b'Aamir Khan')]),
        ),
    ]
