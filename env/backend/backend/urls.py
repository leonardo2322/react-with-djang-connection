from re import template
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'))
    
]
# urlpatterns += [re_path(r'^.*',
#                         TemplateView.as_view(template_name='index.html'))]
