import email
from django.shortcuts import render,redirect

from datetime import date, datetime
from django.contrib import messages,auth
from sqlalchemy import desc
from .models import Complaint, Signup,Accounts


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm




# Create your views here.

def index(request):
    return render(request ,'index.html')

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def login_post(request):
    
    if request.method =='POST':
        user = auth.authenticate(username=request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'Username or password is incorrect!'})
    
    else:
        return render(request,"login.html", {'error': 'Username or password is incorrect!'})
    
def signup_post(request):
    if request.method =="POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = Accounts.object.create_user(email=email,username=username,fullname=fullname,password=password)
        user.save()
        return render(request,"index.html")
        
    
    return render(request,"signup.html")

def complaint_post(request):
    if request.method=="POST":
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        description= request.POST['description']
        print(name,phone_number,email,description)
        complaint = Complaint(name=name, email=email, phone_number=phone_number,description=description, date= datetime.today() )
        complaint.save()

    return render(request,"complaint.html")

def logout_post(request):
    auth.logout(request)
    return redirect('/login')