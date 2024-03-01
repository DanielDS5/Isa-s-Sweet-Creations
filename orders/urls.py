from django.urls import path
from . import views

urlpatterns = [
    path("", views.process_order , name = "Process_order"),
]