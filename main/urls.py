from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = "main"

urlpatterns=[
    url("", views.homepage, name="homepage")
]
