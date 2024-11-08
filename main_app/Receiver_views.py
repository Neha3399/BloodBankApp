from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.shortcuts import render, redirect

from main_app.forms import R_request, ReceiverRegister
from main_app.models import Receiver, Receiver_request, feedback


def Receiver_view(request):
    return render(request, "Receiver/Receiver_base.html")

@login_required (login_url='login_view')
def Receiver_req(request):
    data=R_request()
    user1=request.user
    print(user1)
    rcvr=Receiver.objects.get(user=user1)
    print(rcvr.id)

    if request.method == "POST":
        Req=R_request(request.POST)
        if Req.is_valid():
            obj = Req.save(commit=False)
            obj.ReceiverName = rcvr
            obj.save()
    return render(request,"Receiver/request.html",{"form":data})


@login_required(login_url='login_view')
def req_table(request):

    user1=request.user
    data=Receiver.objects.get(user=user1)
    obj=Receiver_request.objects.filter(ReceiverName=data)
    return render(request, "Receiver/table_req.html",{'data':obj} )


@login_required(login_url='login_view')
def rmv_req(request,id):
    data=Receiver_request.objects.get(id=id)
    data.delete()
    return redirect('req_table')

@login_required(login_url='login_view')
def replay(request):
    user1 = request.user
    data = Receiver.objects.get(user=user1)
    obj = feedback.objects.filter(name=data)
    return render(request,"Receiver/replay.html",{"data":obj})

@login_required(login_url='login_view')
def profile_receiver(request):
    user1=request.user
    data= Receiver.objects.get(user=user1)
    return render (request,"Receiver/profile.html",{'form':data})

@login_required(login_url='login_view')
def receiver_update(request,id):
    data=Receiver.objects.get(id=id)
    form= ReceiverRegister(instance=data)
    if request.method == "POST":
        profile= ReceiverRegister(request.POST,request.FILES,instance=data)
        if profile.is_valid():
           profile.save()
           return redirect("profile_receiver")
    return render(request,"Receiver/profile_update.html",{"form":form})

def logou(request):
    logout(request)
    return redirect("/")


