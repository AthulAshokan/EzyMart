from django.db import models
from customers.models import Customer
from products.models import Product

# Create oders models

# Model for oder 
class Order(models.Model):
  LIVE=1
  DELETE=0
  DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
  CART_STAGE=0
  ORDER_CONFIRMED=1
  ORDER_PROCESSED=2
  ORDER_DELIVERED=3
  ORDER_REJECTED=4
  STATUS_CHOICE=((ORDER_PROCESSED,"ORDER_PROCESSED"),
                 (ORDER_DELIVERED,"ORDER_DELIVERED"),
                 (ORDER_REJECTED,"ORDER_REJECTEDA"),
                 )
  order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
  owner=models.ForeignKey(Customer,related_name="order",on_delete=models.SET_NULL,null=True)
  delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
  created_at=models.DateTimeField(auto_now_add=True)
  update_at=models.DateTimeField(auto_now=True)

#model for orded item

from .models import Order
class OrdedItem(models.Model):
  product=models.ForeignKey(Product,related_name="orded_item",on_delete=models.SET_NULL,null=True)
  quantiy= models.IntegerField(default=1)
  owner=models.ForeignKey(Order,related_name="added_item",on_delete=models.CASCADE)
  