from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from .forms import RegisterForm

def sign_up(request):
    
    if request.method == "POST":
        
        register_form = RegisterForm(request.POST)
        
        user_email = request.POST["email"]
        db_email = User.objects.filter(email=user_email)

        if register_form.is_valid() and db_email.exists() == False:
            user_account = register_form.save(commit=False)
            user_account.is_active = False
            user_account.save()
            
            return redirect(login_page)
    else:
        register_form = RegisterForm()

    context = {"form":register_form}
    
    return render(request, "app002_auth/sign_up.html", context)

def login_page(request):
    context = {}
    return render(request, "app002_auth/log_in.html", context)

def log_out(request):
    context = {}
    return render(request, "app002_auth/log_out.html", context)
