from django.core.mail import send_mail
from extn import trackie
import simplejson
from goal.tables import ReportTable,MonthTable
import calendar
from gsuggest.models import Post
import datetime as dt
from datetime import datetime, timedelta, tzinfo
from django.views.generic import TemplateView
from django.contrib.auth.models import User
import arrow
import numpy as np
import time
import pandas as pd
import json
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import *
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context, loader, Template, RequestContext
from .models import Report
from django.http import HttpResponse
import csv
from .forms import addReportForm, ExampleForm,FForm
from django.db import connections
from django.db import connection
from django.db.models import *
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.contrib.auth import authenticate, login, logout

#   To the Home Page of the Site


def index(request):
    template = 'login.html'
    c = ''
    Context = ''
    return render(request, template, Context)
def main(request):
    template = 'main.html'
    c = ''
    Context = ''
    return render(request, template, Context)
def login_user(request):
#    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST.get('username', 'username')
        password = request.POST.get('password', 'password')

        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return HttpResponseRedirect('/dashboard')
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main')
        return render_to_response('dashboard/code/error.html', context_instance=RequestContext(request))
    return render_to_response('login.html', context_instance=RequestContext(request))


#   To add the Report of Every pther P'rocess/Persons
@login_required(login_url='/login/')
def add(request):
    c = len(Report.objects.filter(date = time.strftime("%Y-%m-%d")))
    n = Report.objects.filter(date = time.strftime("%Y-%m-%d"))
    form = addReportForm(request.POST)
    if form.is_valid():
        s = form.save(commit=False)
        form.save()
        return HttpResponseRedirect('')
    else:
        form = addReportForm()
    context = {
        "form": form,
        "c" : c,
        "d": n
    }
    template = "add.html"
    return render(request, template, context)

#   Working Fine
def export_excel(request):
    dump = Report.objects.all()
    response = HttpResponse(
        '', content_type='application/vnd.ms-excel;charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="Report"' + str(time.asctime( time.localtime(time.time()) ))+'.csv'
    writer = csv.writer(response)
    writer.writerow(
        ['worker', 'date', 'process', 'count', 'errorzs', 'quality', 'details'])
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
def full_view(request):
    data = ReportTable(Report.objects.all())
    return render(request, "full_view.html", {'data': data})

#   SOPs of Evryother Process
def sop(request):
    template = 'sop.html'
    Context = ''
    return render(request, template, Context)

def dash(request, ass_name, ass_process):
    foos = Report.objects.filter(worker=ass_name, process=ass_process)
    data = serializers.serialize('json', foos)
    response_data = json.loads(str(data))
    return HttpResponse(json.dumps(response_data), content_type="application/json")



def month_wise_worker(request,year, month):

    month_name =  calendar.month_abbr[int(month)]

    OverAll_Indiv_Quality = Report.objects.values('worker').annotate(Quality=Avg('quality')).filter(date__month = month).filter(date__year = year)
    OA_t_Quality = [[i['worker'],i['Quality']] for i in OverAll_Indiv_Quality]
    OA_t_Quality_label = [i[0] for i in OA_t_Quality]
    OA_t_Quality_data = [round(i[1],2) for i in OA_t_Quality]


    return render_to_response('month_worker.html', {'OA_t_Quality_label': json.dumps(OA_t_Quality_label),
                                             'OA_t_Quality_data': json.dumps(OA_t_Quality_data),
                                             'workerdata' : OverAll_Indiv_Quality,
                                             'month_name':month_name
                                                })
def month_wise_process(request,year, month):
    month_name =  calendar.month_abbr[int(month)]
    OverAll_Process_Quality = Report.objects.values('process').annotate(Quality=Avg('quality')).filter(date__month = month).filter(date__year = year)
    OA_p_Quality = [[i['process'],i['Quality']] for i in OverAll_Process_Quality]
    OA_p_Quality_label = [i[0][:6] for i in OA_p_Quality]
    OA_p_Quality_data = [round(i[1],2) for i in OA_p_Quality]

    return render_to_response('month_process.html', { 'OA_p_Quality_label': json.dumps(OA_p_Quality_label),
                                             'OA_p_Quality_data': json.dumps(OA_p_Quality_data),
                                             'processdata': OverAll_Process_Quality,
                                             'month_name':month_name
                                                })

@login_required(login_url='/login/')
def search_form(request):
    return render(request, 'search_form.html')

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

def search(request):
    if 'associate' in request.GET and request.GET['associate']:
        ass = request.GET['associate']
        pr = request.GET['process']
        #yr = request.GET['month']

        truncate_date = connection.ops.date_trunc_sql('month', 'date')
        qs = Report.objects.extra({'month':truncate_date})
        report = qs.values('month','process').annotate(Sum('count')).order_by('process').filter(process = pr).filter(worker = ass)

        data_dict = ValuesQuerySetToDict(report)
        data_json = simplejson.dumps(data_dict)

        """

        For D3 Charts notation. Must be Used in v5

        # for i in x:
        #     if i['process']:
        #         del i['process']
        """

        dater_label = [calendar.month_abbr[datetime.strptime(i['month'], '%Y-%m-%d').month] for i in report]
        user_data = [i['count__sum'] for i in report]

        return render(request, 'search.html',{'data': data_json, 'dater_label' : json.dumps(dater_label), 'user_data':json.dumps(user_data),'fulldata' : report})
    else:
        return HttpResponse('Please submit a search term.')
    return render(request, 'search.html',{'data': data_json, 'dater_label' : json.dumps(dater_label), 'user_data':json.dumps(user_data),'fulldata' : report})


def dashboard(request):
    updates = [i for i in Post.objects.all()]
    w_quality = Report.objects.values('worker').annotate(Quality=Avg('quality')).order_by('worker')
    t_quality = Report.objects.values('process').annotate(Quality=Avg('quality')).order_by('process')
    rss = trackie()
    c = rss.rss_feed()
    yesterday = dt.date.today() - dt.timedelta(days=1)
    Total_Rec = len(Report.objects.all())
    Yday_qual = Report.objects.values('quality').annotate(Quality = Avg('quality')).filter(date = yesterday)
    Yday_qual_data = sum([i['Quality'] for i in Yday_qual])
    Avg_Q = Report.objects.values('quality')
    l = [i['quality'] for i in Avg_Q]
    Avg_Q_data = round(reduce(lambda x, y: x + y, l) / len(l),3)
    current_user = request.user
    template = 'index.html'
    Context = { 'Total_Rec' : Total_Rec,
    'Avg_Q_data' : Avg_Q_data,
    'Yday_qual_data':Yday_qual_data,
    'current_user_id' : current_user,
    'current_user' : str(current_user) + '@groupon.com',
    'c' : c,
    'updates'  : updates,
    'w_quality':w_quality,
    't_quality' : t_quality,
}
    return render(request, template, Context)
def test(request):
    send_mail('Subject here', 'Here is the message.', 'c_thv@groupon.com',['c_thv@groupon.com'], fail_silently=False)
    template = 'test.html'
    Context = {
    'c1': 'a',
    'c2' :'b'
    }
    return render(request, template, Context)
def chumma(request):
    if request.GET:
        associate = request.GET.get('associate')
        process = request.GET.get('process')
        result = Report.objects.filter(worker = associate, process = process)
        c = [i['quality'] for i in Report.objects.values('quality').filter(worker = associate, process = process)]
        d = reduce(lambda x, y: x + y, c) / len(c)
