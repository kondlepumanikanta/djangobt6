# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app2.models import StudyHall,Expenses,Course,Student,Enquiry
# Register your models here.
admin.site.register(StudyHall)
admin.site.register(Expenses)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Enquiry)


