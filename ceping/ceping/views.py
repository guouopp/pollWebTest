#coding=utf-8
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return redirect(reverse("ceping_login"))


def logouts(request):
    logout(request)
    return redirect(reverse("ceping_login"))


def logins(request):
    if request.method == "GET":
        return render(request, "login.html", locals())
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse("poll_index"))
            else:
                login_error_msg = '账号已停用'
        else:
           login_error_msg = '用户名或密码错误'
        return render(request, "login.html", locals())


@login_required
@csrf_exempt
def password(request):
    if request.method == "GET":
        return render(request, "password.html", locals())
    else:
        old = request.POST.get("old_password")
        new = request.POST.get("new_password")
        user = User.objects.get(id=request.user.id)
        if user.check_password(old):
            msg = "<font style='color:red'>原密码不正确!</font>"
        else:
            user.set_password(new)
            user.save()
            msg = "<font style='color:green'>密码修改成功, 下次登录时, 请使用新密码!</font>"
        return render(request, "password.html", locals())



