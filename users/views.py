from django.shortcuts import render, redirect
from .models import RegisterForm, AuthToken
# Create your views here.



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            instance = form.save()
            myuser  = AuthToken(user=instance)
            myuser.save()
            return redirect('web-login') 
        
    else:
        form = RegisterForm()

    return render(request,'users/register.html',{'form':form})
