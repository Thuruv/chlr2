# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0021_auto_20150901_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='process',
            field=models.CharField(default=b'Select Something', max_length=40, verbose_name=b'What Process?', choices=[(b'Select Something', b'Select Something'), (b'Mid Night Site Check', b'Mid Night Site Check'), (b'Item Attributes', b'Item Attributes'), (b'Mass Refunds', b'Mass Refunds'), (b'EOD Check', b'EOD Check'), (b'Ideeli', b'Ideeli'), (b'Product- Updates', b'Product- Updates'), (b'OI Cloning', b'OI Cloning'), (b'OI Vetting', b'OI Vetting'), (b'App-Ops (User Management/Carriers)', b'App-Ops (User Management/Carriers)'), (b'App-Ops (Offboarding/SOx', b'App-Ops (Offboarding/SOx)'), (b'Store Merchants', b'Store Merchants'), (b'Ad Hoc', b'Ad Hoc'), (b'Historical Taxonomization Rolling Queue', b'Historical Taxonomization Rolling Queue'), (b'Historical Taxonomization', b'Historical Taxonomization')]),
        ),
    ]
