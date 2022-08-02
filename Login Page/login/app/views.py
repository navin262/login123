from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import form

def index(request):
    if request.method=="POST":
        name=request.POST['lname']
        email=request.POST['email']
        password=request.POST['Password']
        reg=form(name=name, email=email, password=password)
        reg.save()
        return render(request,"login.html")
    else:
        pass
    return render(request,"index.html")

def login(request):
    try:
        if request.method=="POST":
            username=request.POST['lname']
            password=request.POST['Password']
            user=form.objects.filter(name=username,password=password)
            k=user[0]
            if k is not None:
                return HttpResponseRedirect("/wel/")
        else:
            return render(request,"login.html")
    except:                
       return render(request,"login.html")

def wel(request):
    return render(request,"wel.html")


# Create your views here.
