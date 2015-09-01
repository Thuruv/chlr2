# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0002_auto_20150821_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='ass',
            new_name='worker',
        ),
        migrations.AlterField(
            model_name='associate',
            name='employee',
            field=models.CharField(max_length=25, verbose_name=b'Whois it?', choices=[(b'Thiliban', b'Thiliban'), (b'Ramachandran', b'Ramachandran'), (b'Sathish', b'Sathish'), (b'Pradeep', b'Pradeep Anand'), (b'Prathipa', b'Prathipa'), (b'Madhan', b'Madhan'), (b'Gayathri', b'Gayathri'), (b'Karthick', b'Karthick'), (b'Aqhil Mohammad', b'Aqhil Mohammad'), (b'Soniya', b'Soniya'), (b'Aamir Khan', b'Aamir Khan')]),
        ),
        migrations.AlterField(
            model_name='report',
            name='process',
            field=models.CharField(max_length=30, verbose_name=b'What Process?', choices=[(b'Mid Night Site Check', b'Mid Night Site Check'), (b'Item Attributes', b'Item Attributes'), (b'Mass Refunds', b'Mass Refunds'), (b'EOD Check', b'EOD Check'), (b'Ideeli', b'Ideeli'), (b'Product- Updates', b'Product- Updates'), (b'OI Cloning', b'OI Cloning'), (b'OI Vetting', b'OI Vetting'), (b'App-Ops (User Management/Carriers)', b'App-Ops (User Management/Carriers)'), (b'App-Ops (Offboarding/SOx', b'App-Ops (Offboarding/SOx'), (b'Store Merchants', b'Store Merchants'), (b'Ad Hoc', b'Ad Hoc')]),
        ),
    ]
