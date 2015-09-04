from django.contrib import admin
from import_export import fields
from daterange_filter.filter import DateRangeFilter
from .models import  Report
from .forms import addReportForm
from import_export.admin import ImportExportModelAdmin

class ReportAdmin(admin.ModelAdmin):
    list_display = ['worker', 'date', 'process', 'count', 'errorz','quality','details']
    list_filter = (
        'worker', ('date', DateRangeFilter), 'process'
    )
    form = addReportForm

admin.site.register(Report,ReportAdmin)
