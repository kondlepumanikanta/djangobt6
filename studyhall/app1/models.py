# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class StudyHall(models.Model):
	name=models.CharField(max_length=50)
	area=models.TextField()
	class Meta:
		db_table="studyhall"
class Enquiries(models.Model):
	name=models.CharField(max_length=50)
	contactnum=models.IntegerField()
	course=models.CharField(max_length=50)
	class Meta:
		db_table="enquiries"
class Expenses(models.Model):
	name=models.CharField(max_length=50)
	dateofexp=models.DateField(auto_now=True)
	# reading_room=models.CharField(max_length=50)
	reading_room=models.ForeignKey(StudyHall)
	sumofexp=models.IntegerField()
	class Meta:
		db_table="expenses"

