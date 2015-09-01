from __future__ import division
import django_filters
from django.db import models
import time
import datetime
from decimal import Decimal
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType

data_associates = (
    ('Venkat','Venkat'),
    ('Select Something','Select Something'),
    ('Thiliban','Thiliban'),
    ('Ramachandran','Ramachandran'),
    ('Sathish','Sathish'),
    ('Pradeep Anand','Pradeep Anand'),
    ('Prathipa','Prathipa'),
    ('Madhan','Madhan'),
    ('Gayathri','Gayathri'),
    ('Karthick','Karthick'),
    ('Aqhil Mohammad','Aqhil Mohammad'),
    ('Soniya','Soniya'),
    ('Aamir Khan','Aamir Khan')
)

data_process = (
                    ('Select Something','Select Something'),
                    ('Mid Night Site Check','Mid Night Site Check'),
                    ('Item Attributes','Item Attributes'),
                    ('Mass Refunds','Mass Refunds'),
                    ('EOD Check','EOD Check'),
                    ('Ideeli','Ideeli'),
                    ('Product- Updates','Product- Updates'),
                    ('OI Cloning','OI Cloning'),
                    ('OI Vetting','OI Vetting'),
                    ('App-Ops (User Management/Carriers)',\
                    'App-Ops (User Management/Carriers)'),
                    ('App-Ops (Offboarding/SOx','App-Ops (Offboarding/SOx)'),
                    ('Store Merchants','Store Merchants'),
                    ('Ad Hoc','Ad Hoc')
                )


class Report(models.Model):
    worker  = models.CharField('Whois it?',choices = data_associates, default = 'Select Something', max_length = 25)
    date = models.DateField('Report Date', default =time.strftime("%d/%m/%Y") )
    process = models.CharField('What Process?',choices = data_process, default = 'Select Something', max_length = 30)
    count = models.IntegerField('The Count', default=0)
    error = models.IntegerField('Errors Made', default= 0)
    quality = models.FloatField('The Qulaity', default=0.0)
    details = models.CharField('Any Details to Dump', blank = True ,max_length = 256)

    def __unicode__(self):
        return str(self.worker)
        return self.date
        return str(self.process)
        return self.count
        return self.error
    def qual(self):
        #   with __future__ you scum ..!!
        #   100-((38/150)*100)
        equal = 100 - ((self.error / self.count) * 100)
        return "{:.2f}".format(equal)

    def save(self):
        self.quality = self.qual()
        super(Report, self).save()

class CustomFilter(django_filters.FilterSet):
    class Meta:
        model = Report
        fields = ['worker', 'date', 'process']

def get_admin_url(self):
    content_type = ContentType.objects.get_for_model(self.__class__)
    return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))
