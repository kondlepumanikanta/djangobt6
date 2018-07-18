# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from app1.models import StudyHall
from app1.models import Enquiries
from app1.models import Expenses

# Create your views here.
def studhall(request):
	
	stud=StudyHall.objects.all()
	expns=Expenses.objects.all()
	enq=Enquiries.objects.all()
	#return render(request,"app1/index.html",{"halls":studyhalls,"exps":expenses,"enqs":enquiries})

	#return render(request,"app1/index.html")
	return render(request,"app1/index.html",{"studyhall_data":stud})
def enquiries(request):
	enq=Enquiries.objects.all()
	return render(request,"app1/index.html",{"enquiries_data":enq})
def expenses(request):
	exp=Expenses.objects.all()
	return render(request,"app1/index.html",{"expenses_data":exp})