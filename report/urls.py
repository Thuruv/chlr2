from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from goal import views
from gsuggest import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.defaults import page_not_found
from django.views.generic import TemplateView

urlpatterns = [
# Examples:

url(r'^main/$', 'goal.views.main'),
url(r'^login/$', 'goal.views.login_user'),
url(r'^contact/',    include('envelope.urls')),
url(r'^$', RedirectView.as_view(url='login/', permanent=False), name='index'),
#url(r'^$', 'goal.views.index', name='index'),
url(r'^admin/', include(admin.site.urls)),
url(r'^add/', 'goal.views.add', name='add'),
url(r'^sop/', 'goal.views.sop', name='sop'),
url(r'^report/ass/(\d{4})/(\d)/$', 'goal.views.month_wise_worker', name='month_wise_worker'),
url(r'^report/process/(\d{4})/(\d)/$', 'goal.views.month_wise_process', name='month_wise_process'),
url(r'^view/', 'goal.views.full_view', name='full_view'),
url(r'^export/', 'goal.views.export_excel', name='export_excel'),
url(r'^test/', 'goal.views.test', name='test'),
url(r'^dashboard/', 'goal.views.dashboard', name='dashboard'),
url(r'^search_form/$', 'goal.views.search_form',name = 'search_form'),
url(r'^search/$',  'goal.views.search',name = 'search'),
url(r'^dash/(?P<ass_name>/<ass_process>\w+)/$', 'goal.views.dash', name='dash'),
url(r'^post/(?P<post_id>\d+)/detail.html$',
   'gsuggest.views.post_detail', name='post_detail'),
url(r'^post/upload$', 'gsuggest.views.post_upload', name='post_upload'),
url(r'^post/all$', 'gsuggest.views.all_view', name='all_view'),
]
