# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0020_auto_20150901_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='error',
            new_name='errorz',
        ),
    ]
