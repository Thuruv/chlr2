from django import forms
from django.forms import ModelForm
from .models import Report



class addReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['worker', 'date', 'process', 'count', 'errorz','details']
    def __init__(self, *args, **kwargs):
        super(addReportForm, self).__init__(*args, **kwargs)

class RatingForm(forms.ModelForm):
    def __init__(self, current_user, *args, **kwargs):
        super(RatingForm, self).__init__(*args, **kwargs)
        #self.fields['process'].queryset = self.fields['process'].queryset.exclude(id=current_user.id)

    class Meta:
        model = Report
        fields = ['worker', 'date', 'process', 'count', 'errorz']
