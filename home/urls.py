from django.contrib import admin
from django.urls import path
from django.urls import include, path, re_path
from django.conf import settings
from django.views.static import serve
from . import views
static_urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('begins', views.forms, name='forms'),
    path("exercise/<slug>", views.exercise, name='exercise'),
    path("prepare", views.prepare, name="prepare"),
    path("calculate", views.calculate, name="calculate"),
    path("", include(static_urlpatterns)),
]