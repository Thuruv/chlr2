from django.conf.urls import include, url
from django.contrib import admin
from goal import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]
