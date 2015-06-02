#coding=utf-8
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from officesupply.models import Material, UseRecord
from staff.models import Staff


@login_required
def index(request):
    materials = Material.objects.all().order_by("name")
    return render(request, "officesupply/index.html", locals())


@login_required
@csrf_exempt
def sign(request):
    try:
        num = int(request.POST.get("num"))
        material_id = request.POST.get("material_id")
        material = Material.objects.get(id=int(material_id))
        staff = Staff.objects.get(user=request.user)
        #先减掉库存, 并保存
        material.stock -= num
        material.save()
        #再保存领取记录
        ur = UseRecord(staff=staff, material=material, number=num)
        ur.save()
        return HttpResponse("ok")
    except Exception, e:
        return HttpResponse("error:%s" % e)

