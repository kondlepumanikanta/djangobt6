# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Vegetables(models.Model):
		name=models.CharField(max_length=250)
		cost=models.IntegerField()
		class Meta:
			db_table="vegetables"
