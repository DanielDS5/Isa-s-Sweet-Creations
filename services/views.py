from django.shortcuts import render
from .models import cakes

# Create your views here.

def offers(request):
    
    cake = cakes.objects.all()
    
    return render(request, 'offers.html', {"cakes": cake})
