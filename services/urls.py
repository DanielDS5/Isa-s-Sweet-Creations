from django.urls import path
from services import views

urlpatterns = [
    path("", views.offers, name = "Offers"),
]