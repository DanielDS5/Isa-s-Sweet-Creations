from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

class ViewsRegister(View):
    
    def get(self, request):    
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("Home")
        
        else:
            for i in form.error_messages:
                messages.error(request, i)    
                
            return render(request, "register.html", {"form": form})
        
def close_session(request):
    logout(request)
    
    return redirect("Home")

def login_session(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                messages.error(request, "Usuario no válido")
                
        else:
            messages.error(request, "Información Incorrecta")
            
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})
