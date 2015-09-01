from django.db import models

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

class Post(models.Model):
    content = models.TextField(max_length=256)
    created_at = models.DateField('Datetime created', blank = True)
    process = models.CharField(choices = data_process, max_length = 50, default = 'Select Something')
    def __unicode__(self):
        return self.content
        return self.content
        return self.process
