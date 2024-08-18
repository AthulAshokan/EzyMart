from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Customer


# Create your views here.

def customer_accout(request): 
  if request.POST and 'register' in request.POST :
    try:
      username = request.POST.get('username')
      email = request.POST.get('email')
      password = request.POST.get('password')
      address = request.POST.get('address')
      phone = request.POST.get('phone') 

      #  create user account
      user=User.objects.create_user(
        username=username,
        password=password,
        email=email
      )
      # create customer account
      customer = Customer.objects.create(
              phone=phone,
              address=address,
              user=user,
              
      )
      return redirect('home_page')
    except Exception as e:
      error_message="duplicate invalid username"
      messages.error(request, error_message)

  if request.POST and 'login' in request.POST:
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username,password=password)
    if user: 
      login(request,user)
      return redirect("home_page")
    else:
        messages.error(request,"Invalid username or password." ) 
  
  return render(request,"account.html")





  




