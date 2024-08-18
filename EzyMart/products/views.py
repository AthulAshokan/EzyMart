from django.shortcuts import render
from products.models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
  feature_products = Product.objects.order_by('-priority')[ :4]
  latest_products = Product.objects.order_by('id')[ :4]
  context = {
    'feature_products':feature_products,
    'latest_products':latest_products
  }
  return render(request,'index.html',context)

def product_list(request):
  """return product list"""
  page=1
  if request.GET:
    page=request.GET.get("page",1)
  list_product = Product.objects.order_by('-priority')
  Product_paginator=Paginator(list_product,2)
  list_product=Product_paginator.get_page(page)
  context = {"products":list_product}
  return render(request,'products.html',context)


def product_detail(request,pk):
  product_detail = Product.objects.get(pk=pk)
  context={'product':product_detail}
  return render(request,"product_detail.html",context)

