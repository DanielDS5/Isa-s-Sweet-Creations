from cart.cart import Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Order, OrderLine

# Create your views here.

@login_required(login_url="/authentication/login")
def process_order(request):
    order = Order.objects.create(user=request.user)
    cart = Cart(request)
    orderslines = list()
    
    for k, v in cart.cart.items():
        orderslines.append(OrderLine(
            user=request.user,
            product_id=k,
            order_id= order,
            amount=v["amount"],
            
        ))
        
    OrderLine.objects.bulk_create(orderslines)
    
    try:
        send_email(
        order=order,
        order_line = orderslines,
        username = request.user.username,
        email = request.user.email
        )
    
        messages.success(request, "Pedido Recibido")
        
    except:
        print(order, ordersline)
    
    return redirect("Shop")
    
def send_email(order, order_line, username, email):
    topic = "Pedido Recibido"
    message = render_to_string("email/order.html", {
        "order": kwargs.get("order"),
        "orderslines": kwargs.get("order_line"),
        "username": kwargs.get["username"]
    })
    
    text_message = strip_tags(message)
    
    from_mail = "Isas@SweetCreations.com"
    to = kwargs.get("email")
    
    send_mail(topic, text_message, from_email, [to], html_message=message)
