# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0005_auto_20150822_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='addedon',
        ),
    ]
