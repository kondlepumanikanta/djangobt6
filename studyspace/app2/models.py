# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class StudyHall(models.Model):
	name = models.CharField(max_length=50)
	area = models.TextField(max_length=250)
	def __str__(self):
		return "%s|%s"%(self.name, self.area)

class Expenses(models.Model):
	studyhall = models.ForeignKey(StudyHall)
	date = models.DateTimeField()
	name=models.CharField(max_length=250)
	desc = models.TextField(max_length=250)
	value= models.IntegerField()

	def __str__(self):
		return "%s,%s,%s,%s"%(self.studyhall, 
			self.date, 
			self.value,
		 	self.desc)

class Course(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name
class Student(models.Model):
	name=models.CharField(max_length=250)
	address = models.TextField(max_length=250)
	phone = models.CharField(max_length=10)
	email = models.CharField(max_length=250)

	def __str__(self):
		return self.name


class Enquiry(models.Model):
	name = models.CharField(max_length=250)
	course = models.ForeignKey(Course)
	student = models.ForeignKey(Student)
	def __str__(self):
		return "%s,%s,%s"%(self.name,self.student,self.course)




'''from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Studyhall(models.Model):
	name=models.CharField(max_length=250)
	area=models.TextField()
	def __str__(self):
		return "%s|%s"%(self.name, self.area)
class Expenses(models.Model):
	name=models.CharField(max_length=50)
	dofexp=models.DateTimeField(auto_now=True)
	studyhall=models.ForeignKey(Studyhall)
	desc=models.CharField(max_length=250)
	value=models.IntegerField()
	#reading_room=models.ForeignKey(Studyhall)
	#sum_exp=models.IntegerField()
	def __str__(self):
		return "%s,%s,%s,%s"%(self.name,self.dofexp,self.studyhall,self.desc,self.value)
class Course(models.Model):
	name=models.CharField(max_length=250)
	def __str__(self):
		return self.name
class Student(models.Model):
	name=models.CharField(max_length=250)
	phone=models.IntegerField()
	address=models.TextField(max_length=250)
	email=models.CharField(max_length=250)
	def __str__(self):
		return "%s,%s,%s,%s"%(self.name,self.phone,self.address,self.email)
class Enquiry(models.Model):
	name=models.CharField(max_length=250)
	#phone=models.IntegerField()
	#course=models.TextField()
	course=models.ForeignKey(Course)
	student=models.ForeignKey(Student)
	def __str__(self):
		return "%s,%s,%s"%(self.name,self.course,self.student)
'''