from django.shortcuts import render
from .models import Post

# Create your views here.

def cakes(request):
    
    posts = Post.objects.all()
    
    return render(request, 'cakes.html', {'posts': posts})
