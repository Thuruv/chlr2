from django.contrib import admin

from models import Post
from import_export import fields
from daterange_filter.filter import DateRangeFilter
from import_export.admin import ImportExportModelAdmin
from .forms import PostModelForm
from admin_exporter.actions import export_as_csv_action




class ReportAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_at', 'process']
    list_filter = (
        ('created_at', DateRangeFilter), 'process'
    )
    form = PostModelForm
admin.site.register(Post,ReportAdmin)
admin.site.add_action(export_as_csv_action)
