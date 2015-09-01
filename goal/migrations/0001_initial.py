# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Associate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee', models.CharField(max_length=25, choices=[(b'Thiliban', b'Thiliban'), (b'Ramachandran', b'Ramachandran'), (b'Sathish', b'Sathish'), (b'Pradeep', b'Pradeep Anand'), (b'Prathipa', b'Prathipa'), (b'Madhan', b'Madhan'), (b'Gayathri', b'Gayathri'), (b'Karthick', b'Karthick'), (b'Aqhil Mohammad', b'Aqhil Mohammad'), (b'Soniya', b'Soniya')])),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'Report Date')),
                ('process', models.CharField(max_length=30, verbose_name=b'Process')),
                ('count', models.IntegerField(default=0, verbose_name=b'The Count')),
                ('error', models.IntegerField(default=0, verbose_name=b'Errors Made')),
                ('ass', models.ForeignKey(to='goal.Associate')),
            ],
        ),
    ]
