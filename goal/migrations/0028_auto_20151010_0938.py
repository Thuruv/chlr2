# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0027_auto_20151009_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateField(default=b'2015-10-10', verbose_name=b'Report Date'),
        ),
        migrations.AlterField(
            model_name='report',
            name='process',
            field=models.CharField(default=b'Select Something', max_length=50, verbose_name=b'What Process?', choices=[(b'Select_Something', b'Select Something'), (b'Mid Night Site Check', b'Mid Night Site Check'), (b'Item Attributes', b'Item Attributes'), (b'Mass Refunds', b'Mass Refunds'), (b'EOD Check', b'EOD Check'), (b'Data-Enrichment', b'Data-Enrichment'), (b'Ideeli', b'Ideeli'), (b'Product Updates', b'Product Updates'), (b'OI Cloning', b'OI Cloning'), (b'OI Vetting', b'OI Vetting'), (b'App-Ops (User Management/Carriers)', b'App-Ops (User Management/Carriers)'), (b'App-Ops (Offboarding/SOx)', b'App-Ops (Offboarding/SOx)'), (b'Store Merchants', b'Store Merchants'), (b'Ad Hoc', b'Ad Hoc'), (b'Price Scrapping', b'Price Scrapping'), (b'Historical Taxonomization Rolling Queue', b'Historical Taxonomization Rolling Queue'), (b'Historical Taxonomization', b'Historical Taxonomization')]),
        ),
    ]
