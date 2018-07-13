# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Customer
from app1.models import Product
from app1.models import SalesOrder



# Create your views here.
def customers(request):
	custs=Customer.objects.all()
	return render(request,"app1/customer.html",{"data":custs})
	
def products(request):
	pros=Product.objects.all()
	return render(request,"app1/product.html",{"data":pros})

def sales(request):
	sals=SalesOrder.objects.all()
	return render(request,"app1/sales.html",{"data":sals})

