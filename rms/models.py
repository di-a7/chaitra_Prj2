from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
   name = models.CharField(max_length=100) # drink

class Food(models.Model):
   name = models.CharField(max_length=100) # coke, pepsi, fanta
   description = models.TextField()
   price = models.IntegerField()
   category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Table(models.Model):
   number = models.CharField(max_length=2)
   capacity = models.CharField(max_length=2)
   is_available = models.BooleanField(default = True)

class Order(models.Model):
   STATUS_CHOICE = [
      ('P','Pending'),
      ('C','Compelete'),
      ('D','Delivered')
   ]
   payment_status = [
      ('P','PAID'),
      ('U','PENDING')
   ]
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   total_price = models.IntegerField()
   status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='P')
   payment_status = models.CharField(max_length=1, choices=payment_status, default='P')

class OrderItem(models.Model):
   order = models.ForeignKey(Order, on_delete=models.PROTECT)
   food = models.ForeignKey(Food, on_delete=models.PROTECT)