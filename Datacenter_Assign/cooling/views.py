# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
def fun(request):
	return HttpResponse("25.67")

def fun1(request):
		res="""
<html>
<head>
  <tittle>
   tittle="django"
  </tittle>
</head>
<body bg color="#52965d">
   this is main part
   <h1>
    this is an h1 tag
   </h1>
   <h2>
   	this is h2 tag
   </h2>
   <h3>
    this is an h3 tag
   </h3>
   <h4>
   	this is h4 tag
   </h4>
   <h5>
    this is an h5 tag
   </h5>
   <h6>
   	this is h6 tag
   </h6>
   <a href="www.gotogoogle.com">gotogoogle</a><br>
   <a href="www.youtube.com">gotoyoutube</a><br>
   <a href="www.yahoo.com">gotoyahoo</a><br>
   <a href="www.linkedin.com">linkedin</a><br>
   <a href="www.gmail.com">gmail</a><br>
   <a href="www.instagram.com">instagram</a><br>
   <form>
   	username:<input type="text"></input><br>
   	password:<input type="password"></input><br>
   	Email:<input type="email"></input><br>
   	Gender:<input type="radio"></input>Female<br>
    Gender:<input type="radio"></input>male<br>
    <input type="text"></input></body><br>
    do you want join immediately<input type="text"></input><br>
   	<input type="submit"></input><br>
   </form>

</body>
</html>

		"""
		return HttpResponse(res)

def fun2(request):
	return render(request,"index.html")
		


# Create your views here.
