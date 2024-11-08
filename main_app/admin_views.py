from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pyexpat.errors import messages

from main_app.forms import DonerRegister, ReceiverRegister, Fdbk
from main_app.models import Login, Doner, Receiver, Receiver_request, feedback

@login_required(login_url='login_view')
def admin_view(request):

     return render(request,"admin/admin_base.html",)

@login_required(login_url='login_view')
def table_view(request):
    data=Doner.objects.all()
    return render(request, "admin/table.html",{'data':data} )

@login_required(login_url='login_view')
def remove(request,id):
    data = Doner.objects.get(id=id)
    data.delete()
    return redirect("admin_view")

@login_required(login_url='login_view')
def update(request,id):
    data= Doner.objects.get(id=id)
    form= DonerRegister(instance=data)
    if request.method == "POST":
        Blood=DonerRegister(request.POST,instance=data)
        if Blood.is_valid():
           Blood.save()
           return redirect("admin_view")
    return render(request,"admin/update.html",{"form":form})

#receiver

@login_required(login_url='login_view')
def table2_view(request):
    data=Receiver.objects.all()
    return render(request, "admin/table2.html",{'data':data} )

@login_required(login_url='login_view')
def remove2(request,id):
    data = Receiver.objects.get(id=id)
    data.delete()
    return redirect("admin_view")

@login_required(login_url='login_view')
def update2(request,id):
    data= Receiver.objects.get(id=id)
    form= ReceiverRegister(instance=data)
    if request.method == "POST":
        Blo=ReceiverRegister(request.POST,instance=data)
        if Blo.is_valid():
           Blo.save()
           return redirect("admin_view")
    return render(request,"admin/update2.html",{"form":form})

@login_required(login_url='login_view')
def req_admin(request):
    obj=Receiver_request.objects.all

    return render(request, "admin/table_req.html",{'data':obj} )

@login_required(login_url='login_view')
def Donor_accept(request):

    obj = Receiver_request.objects.filter(Status=1)
    return render(request,"admin/donation_accept.html",{'data':obj})

@login_required(login_url='login_view')
def accept(request,id):
    obj =Receiver_request.objects.get(id=id)
    obj.Status = 2
    obj.save()
    return redirect('Donor_accept')

@login_required(login_url='login_view')
def reject(request,id):
    obj=Receiver_request.objects.get(id=id)
    obj.Status = 0
    obj.save()
    return redirect('Donor_accept')

@login_required(login_url='login_view')
def accept_view(request):
    data = Receiver_request.objects.filter(Status=2)
    return render(request,"admin/accept.html",{"data":data})

@login_required(login_url='login_view')
def feedbk(request):
    data = Fdbk()
    user1 = request.user
    rcvr = Receiver.objects.get(user=user1)


    if request.method == "POST":
        Req = Fdbk(request.POST)
        if Req.is_valid():
            obj = Req.save(commit=False)
            obj.name = rcvr
            obj.save()

    return render(request,"admin/feedback.html",{"data":data})

@login_required(login_url='login_view')
def replay_view(request):
    data = feedback.objects.all()
    return render(request,"admin/replay.html",{"data":data})

@login_required(login_url='login_view')
def replay_feedback(request,id):
    Feedbak=feedback.objects.get(id=id)
    if request.method == "POST":
        r = request.POST.get('replay')
        Feedbak.replay = r
        Feedbak.save()

        # messages.info(request,"replay send ")
        return redirect('replay_view')
    return render(request,"admin/reply_feed.html",{'Feedbak':Feedbak})

def logou(request):
    logout(request)
    return redirect("/")