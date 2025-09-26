from django.urls import path, re_path

from . import views

app_name = "gallery"
urlpatterns = [
    re_path(r"^delete/(?P<pk>\d+)/$", views.delete, name="delete"),
    path("", views.index, name="index"),
]
