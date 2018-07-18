# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class StudyHall(models.Model):
	name=models.CharField(max_length=50)
	area=models.TextField()
	def __str__(self):
		return "%s%s"%(self.name,self.area)
	class Meta:
		db_table="studyhall"
class Course(models.Model):
	name=models.CharField(max_length=250)
	def __str__(self):
		return self.name
	class Meta:
		db_table="course"
	
class Student(models.Model):
	name=models.CharField(max_length=250)
	address=models.TextField(max_length=250)
	phonenum=models.CharField(max_length=10)
	email=models.CharField(max_length=250)
	def __str__(self):
		return self.name
class Enquiries(models.Model):
	name=models.CharField(max_length=50)
	#contactnum=models.IntegerField()
	course=models.ForeignKey(Course)
	student=models.ForeignKey(Student)
	def __str__(self):
		return "%s,%s,%s"%(self.name,self.student,self.course)
	class Meta:
		db_table="enquiries"


class Expenses(models.Model):
	name=models.CharField(max_length=50)
	dateofexp=models.DateTimeField(auto_now=True)
	# reading_room=models.CharField(max_length=50)
	reading_room=models.ForeignKey(StudyHall)
	#sumofexp=models.IntegerField()
	desc=models.TextField(max_length=250)
	value=models.IntegerField()
	def __str__(self):
		return "%s,%s,%s,%s"%(self.studyhall,self.dateofexp,self.desc,self.value)
	class Meta:
		db_table="expenses"

