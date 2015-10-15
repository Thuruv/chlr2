from django import forms
from django.forms import ModelForm
from .models import Report
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit



class addReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['worker', 'date', 'process', 'count', 'errorz','details']
    def __init__(self, *args, **kwargs):
        super(addReportForm, self).__init__(*args, **kwargs)

class ExampleForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                'notes'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )
class FForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['process','worker']