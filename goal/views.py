import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context, loader, Template, RequestContext
from .models import Report, CustomFilter
from django.http import HttpResponse
import csv
from .forms import addReportForm
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
def sop(request):
    context = {
    }
    template = "sop.html"
    return render(request,template,context)

# Test project
def dash(request):
    fig = Figure()
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("C:/Users/c_thv/desktop/django.csv")
    data_df = pd.DataFrame(data_df)
    data_df.plot(ax=ax)
    canvas = FigureCanvas(fig)
    response = HttpResponse( content_type = 'image/png')
    canvas.print_png(response)
    return response
