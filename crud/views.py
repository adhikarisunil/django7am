from django.shortcuts import render,redirect
from . models import Student
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Student.objects.create(name=name, email=email, phone=phone)
        messages.success(request, 'Student added successfully')
        return redirect('index')
    
    else:
        data = {
            'students': Student.objects.all()
        }
        return render(request, 'index.html', data)