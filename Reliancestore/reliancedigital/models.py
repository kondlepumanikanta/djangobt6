# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Institute(models.Model):
	name=models.CharField(max_length=250)
	cost=models.IntegerField()
	class Meta:
		db_table="Institute"d:
class Student(models.Model):
	name=models.CharField(max_length=250)
	address=models.TextField()
	class Meta:
		db_table="Student"
class Course(models.Model):
	course_types=[('online',"onlinemode"),('offline',"offline")]
	name=models.CharField(max_length=250)
	institute=models.ManyToManyField(Institute)
	student=models.ForeignKey(Student)
	cour_type=models.CharField(choices=course_types,max_length=10)
	class Meta:
		db_table="Course"