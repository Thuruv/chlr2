from django.conf.urls import include, url
from django.contrib import admin
from goal import views
from gsuggest import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.defaults import page_not_found
from rest_framework.urlpatterns import format_suffix_patterns
#<link rel="stylesheet" type="text/css" href="{% static 'some.css' %}" />

urlpatterns = [
# Examples:
# url(r'^$', 'report.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
#url(r'^goal/', include('goal.urls')),
url(r'^gindex', 'gsuggest.views.gindex', name='gindex'),
url(r'^$', 'goal.views.index', name='index'),
url(r'^admin/', include(admin.site.urls)),
url(r'^add/', 'goal.views.add', name='add'),
url(r'^view/', 'goal.views.custom_list', name='custom_list'),
url(r'^export/', 'goal.views.export_excel', name='export_excel'),
url(r'^sop/', 'goal.views.sop', name='sop'),
url(r'^dash/', 'goal.views.dash', name='dash'),
url(r'^post/(?P<post_id>\d+)/detail.html$',
    'gsuggest.views.post_detail', name='post_detail'),
url(r'^post/upload$', 'gsuggest.views.post_upload', name='post_upload'),
url(r'^post/all$', 'gsuggest.views.all_view', name='all_view'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
