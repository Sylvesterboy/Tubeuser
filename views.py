from django.shortcuts import render,redirect
from testapp.models import Customer
from testapp.forms import *
from testapp.models import MyVideos

# Create your views here.
def show(request):
    customer=Customer.objects.all()
    return render(request,'testapp/show.htm',{'cus':customer})

def register(request):
    form=CustomerForm()
    if request.method=='POST':
        form=CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/show')    
    return render(request,'testapp/register.htm',{'form':form})

def delete(request,id):
    emp=Customer.objects.get(id=id)
    emp.delete()
    return redirect('/show')

def update(request,id):
    emp=Customer.objects.get(id=id)
    if request.method=='POST':
        form=CustomerForm(request.POST,request.FILES,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('/show')    
        else:
            return redirect('/register')
    return render(request,'testapp/update.htm',{'emp':emp})                

def home(request):
    videos = MyVideos.objects.all()
    if request.method=='POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email=='admin@gmail.com' and password=='123@123':
            return redirect('/show')
        else:
            return render(request,'testapp/home.htm',{'videos':videos,'error':'Sorry Login has failed.'})
    return render(request,'testapp/home.htm',{'videos':videos})

def asv(request):
    videos = MyVideos.objects.all()
    return render(request,'testapp/showvideos.htm',{'videos':videos})

def v_delete(request,id):
    videos = MyVideos.objects.get(id=id)
    videos.delete()
    return redirect('/asv')

def update_video(request,id):
    videos = MyVideos.objects.get(id=id)
    if request.method=='POST':
        form=VideoForm(request.POST,request.FILES,instance=videos)
        if form.is_valid():
            form.save()
            return redirect('/asv')    
        else:
            return redirect('/register')

    return render(request,'testapp/updatevideos.htm',{'v':videos})


