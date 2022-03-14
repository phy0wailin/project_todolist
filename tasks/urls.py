import imp
from unicodedata import name
from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [ 
    path("", views.index, name="index"),
    path("su/submit", views.submit, name="submit"),
    path("pu/pop", views.pop, name="pop")
]