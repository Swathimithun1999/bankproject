from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages,auth
from .models import MoreDetail




# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('newapp:new')  #add next page
        else:
            messages.info(request,"invalid user")
            return redirect('newapp:login')

    return render(request,'login.html')

def register(request):
    if request.method=='POST':

        username=request.POST['username']
        password=request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('newapp:register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('newapp:login')
        else:
            messages.info(request,"password not match")
            return redirect('newapp:register')
        return redirect('/')

    return render(request,'register.html')


def logout(request):
    # auth.logout(request)
    return redirect('/')
def detail(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST.get('gender')
        phoneNumber = request.POST['phoneNumber']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        branch = request.POST['branch']
        account= request.POST['account']
        material =  request.POST.getlist('material[]')
        userDetails = MoreDetail( name=name,dob=dob,age=age,gender=gender,phoneNumber=phoneNumber,email=email,address=address,district=district,branch=branch,account=account,material=material)
        userDetails.save();
        return redirect('newapp:msg')

    return render(request, 'detail.html')


def new(request):
    return render(request,'new.html')

def msg(request):
    return render(request,'msg.html')
