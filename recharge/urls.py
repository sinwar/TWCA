from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
from . import views

urlpatterns = patterns(
    url(r"^$", views.home, name="home"),
    #url(r"^admin/", include(admin.site.urls)),
    #url(r"^account/", include("account.urls")),
)