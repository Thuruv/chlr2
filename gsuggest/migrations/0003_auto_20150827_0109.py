# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsuggest', '0002_auto_20150827_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='process',
            field=models.CharField(default=b'Select Something', max_length=50, choices=[(b'Select Something', b'Select Something'), (b'Mid Night Site Check', b'Mid Night Site Check'), (b'Item Attributes', b'Item Attributes'), (b'Mass Refunds', b'Mass Refunds'), (b'EOD Check', b'EOD Check'), (b'Ideeli', b'Ideeli'), (b'Product- Updates', b'Product- Updates'), (b'OI Cloning', b'OI Cloning'), (b'OI Vetting', b'OI Vetting'), (b'App-Ops (User Management/Carriers)', b'App-Ops (User Management/Carriers)'), (b'App-Ops (Offboarding/SOx', b'App-Ops (Offboarding/SOx)'), (b'Store Merchants', b'Store Merchants'), (b'Ad Hoc', b'Ad Hoc')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(verbose_name=b'Datetime created', blank=True),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
