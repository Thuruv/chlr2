import json
from chartit import DataPool, Chart
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context, loader, Template, RequestContext
from .models import Report, CustomFilter
from django.http import HttpResponse
import csv
from .forms import addReportForm

#   To the Home Page of the Site
def index(request):
        template = 'homepage.html'
        c = ''
        Context = {
        'post': c
        }
        return render(request, template , Context)
#   To add the Report of Every pther P'rocess/Persons
def add(request):
    form = addReportForm(request.POST or None)
    if form.is_valid():
        s = form.save(commit = False)
        s.save()
        return HttpResponseRedirect('')
    else:
        form = addReportForm()
    context = {
    "form" : form
    }
    template = "add.html"
    return render(request,template,context)

def whole_view(request):
    try:
        c = Report.objects.all().order_by('date')
    except Report.DoesNotExist:
        raise Http404
    template = 'whole_view.html'
    Context = {
    'post': c
    }
    return render(request, template , Context)

#   Working Fine
def export_excel(request):
    dump = Report.objects.all()
    response = HttpResponse('', content_type='application/vnd.ms-excel;charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="Report.csv"'

    writer = csv.writer(response)
    writer.writerow(['worker','date','process', 'count', 'errors', 'quality', 'details'])
    for i in dump:
        writer.writerow([
        i.worker,
        i.date,
        i.process,
        i.count,
        i.error,
        i.quality,
        i.details
        ])

    return response

def custom_list(request):
    filter = CustomFilter(request.GET, queryset=Report.objects.all())
    return render_to_response('custom.html', {'filter': filter})





#@login_required
def chart_data_json(request):
    data = {}
    params = request.GET

    days = params.get('days', 0)
    name = params.get('name', '')
    if name == 'worker':
        data['chart_data'] = Report.get_avg_by_day(
            user=request.user, days=int(days))

    return HttpResponse(json.dumps(data), content_type='application/json')


def sop(request):
    context = {
    }
    template = "sop.html"
    return render(request,template,context)
