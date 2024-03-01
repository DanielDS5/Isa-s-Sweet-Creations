from django.shortcuts import render
from .cart import Cart
from shop.models import Product
from django.shortcuts import redirect

def add_product(request, product_id):
    
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product)
    
    return redirect("Shop")

def delete_product(request, product_id):

    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.delete(product)
    
    return redirect("Shop")   

def substract_product(request, product_id):
    
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.substract(product)
    
    return redirect("Shop")   

def clean_cart(request, product_id):
    
    cart = Cart(request)
    cart.clean()
    
    return redirect("Shop") 