from django_google_charts import charts
from .models import Report

class StepChart(charts.Chart):
    chart_slug = 'steps_chart'
    columns = (
        ('process', "Date"),
        ('worker', "errorz"),
    )

    def get_data(self):
        return Report.objects.values_list('date', 'count')
