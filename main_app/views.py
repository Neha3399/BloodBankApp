from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


from main_app.forms import DonerRegister, LoginRegister, ReceiverRegister, R_request
from main_app.models import Doner


# Create your views here.
def dashboard(request):
    return render(request,"dash.html")
def Login(request):
    return render(request,"login.html")

def DonerR(request, ):
    form1 = LoginRegister()
    form2=DonerRegister()

    if request.method =="POST":
               form1 = LoginRegister(request.POST)
               form2 = DonerRegister(request.POST,request.FILES)

               if form1.is_valid() and form2.is_valid():
                   user1=form1.save(commit=False)
                   user1.is_donor=True
                   user1.save()
                   user2=form2.save(commit=False)
                   user2.user=user1
                   user2.save()
                   return redirect('login_view')
    return render(request,"DonorRegister.html",{"form1":form1,"form2":form2} )

def ReceiverR(request):
    form1 = LoginRegister()
    form2=ReceiverRegister()

    if request.method =="POST":
               form1 = LoginRegister(request.POST)
               form2 = ReceiverRegister(request.POST,request.FILES)

               if form1.is_valid() and form2.is_valid():
                   user1=form1.save(commit=False)
                   user1.is_receiver=True
                   user1.save()
                   user2=form2.save(commit=False)
                   user2.user=user1
                   user2.save()
                   return redirect('login_view')
    return render(request,"ReceiverRegister.html",{"form1":form1,"form2":form2} )

def Land(request):
    return render(request,"index.html")

def login_view(request):
    if request.method == 'POST':
        username= request.POST.get('uname')
        password= request.POST.get('password')
        print(username)
        print(password)
        user= authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            print("ok")
            if user.is_staff:
                print("admin")
                return redirect('admin_view')
            elif user.is_donor:
                print("admin")
                return redirect('Donor_view')
            elif user.is_receiver:
                print("admin")
                return redirect('Receiver_view')
        else:
            messages.info(request,"Invalid credentials")
    return render(request,"login.html")

