# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
def func5(request):
	return HttpResponse("5")
def func05(request):
	res="""
<html>
<head>
	<title>SALES DETAILS</title>
</head>
<body>
<table border="1">
<tr>
	<th>ID</th>
	<th>NAME</th>
	<th>QOH</th>
	<th>OPERATION</th>
	<th>OPERATION</th>
</tr>
<tr>
    <td>1</td>
    <td>raju product</td>
    <td>12</td>
    <td>UPDATE</td>
    <td>DELETE</td>
</tr>
<tr>
	<td>2</td>
	<td>rani product</td>
	<td>13</td>
	<td>UPDATE</td>
	<td>DELETE</td>
</tr>
</table>
</body>
</html>>

	"""
	return HttpResponse(res)
def func005(request):
	return render(request,"tab.html")


# Create your views here.
