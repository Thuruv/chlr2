from django import forms
from django.forms import ModelForm
from .models import Report



class addReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['worker', 'date', 'process', 'count', 'error','details']
    def __init__(self, *args, **kwargs):
        super(addReportForm, self).__init__(*args, **kwargs)
