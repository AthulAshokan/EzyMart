from django.shortcuts import render

# Create your views here.

def user_cart(request):
  return render(request,'cart.html')