
from __future__ import unicode_literals

from __future__ import unicode_literals

from django.shortcuts import render
from app1.models import StudyHall, Expenses, Enquiry, Course, Student, Expenses

# Create your views here.
def view_index(request):
	if request.method=="POST":
		data = request.POST
		if data.get("enquiry"):
			course_inst = Course.objects.get(pk=data.get("enq_course"))
			stdudent_inst = Student.objects.get(pk=data.get("enq_student"))
			enq = Enquiry(
				name = data.get("enq_name"),
				student = stdudent_inst,
				course = course_inst
				)
			enq.save()
		elif data.get("expense"):
			studyhall_inst = StudyHall.objects.get(pk=data.get("exp_studyhall"))
			exp = Expenses(
				studyhall = studyhall_inst,
				date = data.get("exp_date"),
				name = data.get("exp_name"),
				desc = data.get("exp_desc"),
				value = data.get("exp_value"),
				)
			exp.save()
		else:
			hall = StudyHall(name=data.get("hall_name"), 
				area=data.get("hall_area"))
			hall.save()
	studyhalls = StudyHall.objects.all()
	expenses = Expenses.objects.all()
	enquiries = Enquiry.objects.all()
	courses = Course.objects.all()
	students = Student.objects.all()
	return render(request,"app1/index.html",{
		"halls": studyhalls,
		"exps": expenses,
		"enqs": enquiries,
		"students": students,
		"courses": courses 
		})
def view_syudyhalls(request):
	studyhalls = StudyHall.objects.all()
	return render(request,"app1/index.html",{"studyhalls":studyhalls})
'''from django.shortcuts import render
from app1.models import StudyHall, Expenses, Enquiry

# Create your views here.
def view_index(request):
	if request.method=="POST":
		data=request.POST
		#hall=StudyHall(name=request.POST.get('hall_name'),area=request.POST.get('hall_area'))
		#hall.save()
		cour_inst=Course.objects.get(id=request.POST(e_course))
		stud_inst=Student.objects.get(id=request.POST(e_student))
		e_inst=Enquiry(name=data.get('enq_name'),course=cour_inst,student=stud_inst)
		e_inst.save()
		#exps=Expenses(name=request.POST.get('exps_name'),date=request.POST.get('exps_date'),desc=request.POST.get('exps_desc'),value=request.POST.get('exps_value'))
		#exps.save()
		ex_inst=Expenses.objects.get(id=request.POST(ex_studyhall))
		exp_inst=Expenses(studyhall=ex_inst,date=data.get('exp_date'),name=data.get(exp_name),desc=data.get('exp_desc'),value=data.get('exp_value'))
		exp_inst.save()
		
	studyhalls = StudyHall.objects.all()
	expenses = Expenses.objects.all()
	enquiries = Enquiry.objects.all()
	return render(request,"app1/index.html",{
		"halls": studyhalls,
		"exps": expenses,
		"enqs": enquiries 
		})
def view_syudyhalls(request):
	studyhalls = StudyHall.objects.all()
	return render(request,"app1/index.html",{"studyhalls":studyhalls})'''
