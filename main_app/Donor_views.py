from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main_app.filter import BloodFilter
from main_app.forms import DonerRegister
from main_app.models import Receiver_request, Doner

@login_required(login_url='login_view')
def Donor_view(request):
    return render(request, "Donor/Donor_base.html")

@login_required(login_url='login_view')
def req_donor(request):
    obj=Receiver_request.objects.all()
    bloodfilter = BloodFilter(request.GET, queryset=obj)
    data = bloodfilter.qs
    return render(request, "Donor/table_req.html", {'data': data,"bloodfilter":bloodfilter})

@login_required(login_url='login_view')
def Donate(request,id):
    obj=Receiver_request.objects.get(id=id)
    user1 = request.user
    data = Doner.objects.get(user=user1)
    obj.DonerName=data

    obj.Status = 1
    obj.save()
    return redirect("req_donor")

@login_required(login_url='login_view')
def profile_donor(request):
    user1= request.user
    data=Doner.objects.get(user=user1)
    return render (request,'Donor/profile.html',{'form':data})


@login_required(login_url='login_view')
def donor_update(request,id):
    data=Doner.objects.get(id=id)
    form= DonerRegister(instance=data)
    if request.method == "POST":
        profile=DonerRegister(request.POST,request.FILES,instance=data)
        if profile.is_valid():
           profile.save()
           return redirect("profile_donor")
    return render(request,"Donor/profile_update.html",{"form":form})

def logou(request):
    logout(request)
    return redirect("/")