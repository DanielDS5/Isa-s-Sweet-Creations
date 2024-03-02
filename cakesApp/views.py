from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import ContactForm
from cart.cart import Cart

# Create your views here.

def home(request):
    
    cart = Cart(request)
    
    return render(request, 'home.html')

def contact(request):
    
    form = ContactForm()
    
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            telephone = request.POST.get("telephone")
            content = request.POST.get("content")
            
            email = EmailMessage("Message from Django",
                                 f"name: {name} email: {email} telephone: {telephone} \n\n {content}",
                                 "", ["asd.gmail.com"], reply_to = [email])
            
            try:
                email.send()    
                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?invalid")

    return render(request, 'contact.html', {'form': form})