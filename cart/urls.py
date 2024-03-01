from django.urls import path 
from . import views

app_name = "cart"

urlpatterns = [
    path("add/<int:product_id>/", views.add_product, name="add"),
    path("delete/<int:product_id>/", views.delete_product, name="delete"),
    path("substract/<int:product_id>/", views.substract_product, name="substract"),
    path("clean/", views.clean_cart, name="clean"),
    ]
