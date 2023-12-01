from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import Branch
from django.shortcuts import render, redirect




# Create your views here.
def index(request):
    return render(request,'index.html')
#
# def login(request):
#     if request.method =='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             messages.info(request,"invalid bankapp")
#             return redirect('login')
#
#     return render(request,"login.html")
#
#
#
# def register(request):
#     if request.method=='POST':
#         username=request.POST['username']
#
#         password = request.POST['password']
#         cpassword = request.POST['password1']
#
#         if password==cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"Username taken")
#                 return redirect('register')
#
#             else:
#                 user = User.objects.create_user(username=username, password=password)
#                 user.save();
#                 return redirect('login')
#
#         else:
#             messages.info(request,"password not matching")
#             return redirect('register')
#
#         return redirect('/')
#
#     return render(request,"register.html")
# #
# # def register(request):
# #     if request.method =='POST':
# #         username=request.POST['username']
# #         password=request.POST['password']
# #         user=auth.authenticate(username=username,password=password)
# #         if user is not None:
# #             auth.login(request,user)
# #             return redirect('/')
# #         else:
# #             messages.info(request,"invalid bankapp")
# #             return redirect('login')
# #
# #     return render(request,"register.html")
# #
#
#
#
#
#
#
