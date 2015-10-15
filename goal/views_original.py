from graphos.sources.model import ModelDataSource
from graphos.renderers import flot
import json

from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context, loader, Template, RequestContext
from .models import Report, CustomFilter
from django.http import HttpResponse
import csv
from .forms import addReportForm, NameForm
from django.db import connections
from django.db import connection
from django.db.models import *
from django.http import JsonResponse
from django.shortcuts import render

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

#   Working Fine
def export_excel(request):
    dump = Report.objects.all()
    response = HttpResponse('', content_type='application/vnd.ms-excel;charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="Report.csv"'

    writer = csv.writer(response)
    writer.writerow(['worker','date','process', 'count', 'errorzs', 'quality', 'details'])
    for i in dump:
        writer.writerow([
        i.worker,
        i.date,
        i.process,
        i.count,
        i.errorz,
        i.quality,
        i.details
        ])

    return response

#   custom FILTER of the whole Records
def custom_list(request):
    filter = CustomFilter(request.GET, queryset=Report.objects.all())
    return render_to_response('custom.html', {'filter': filter})

#   Sop Download links
# def sop(request):
#
#     context = {
#     }
#     template = "sop.html"
#     return render(request,template,context)
def dash(request):
        #c = [[i.count] for i in Report.objects.filter(process = 'Ideeli')]
        c = Report.objects.all().values('count').values('worker').annotate(Quality=Avg('quality'))
        context = {
        "c" : c
        }
        template = "ch.html"
        return render(request,template,context)
def sop(request):
# Test project
    if request.method == 'GET':
        form = NameForm()
    else:
        # A POST request: Handle Form Upload
        form = NameForm(request.POST) # Bind data from request.POST into a PostForm

        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            content = form.cleaned_data['name']
            #c = Report.objects.all().values('count').values('worker').annotate(Quality=Avg('quality'))
            c = Report.objects.filter('content').values('count').annotate(Quality=Avg('quality'))
    # context = {
    # "c" : c
    # }
    # template = "just.html"
    # return render(request,template,context)
    return render(request, 'just.html', {
        'form': form,
    })
