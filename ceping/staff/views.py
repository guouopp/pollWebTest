#coding=utf-8

from django.shortcuts import render
from staff.models import Staff


def get_staffs(request):
    staffs = Staff.objects.all()
    return render(request, "staff/staff.html", locals())
