from django.urls import path
from . import views

urlpatterns = [
    path("", views.cakes , name = "Cakes"),
]