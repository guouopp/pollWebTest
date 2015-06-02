#coding=utf-8
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from django.shortcuts import render, redirect
from poll.models import Evaluation, EvaluationItems, StaffEvaluation, Items
from staff.models import Staff


@login_required
def index(request):
    return redirect(reverse("poll_best"))

@login_required
def best(request):
    login_staff = Staff.objects.get(user=request.user)
    if login_staff.poll_right:
        staffs = Staff.objects.filter(vote_right=True)
        if request.method == "POST":
            if login_staff.had_poll:
                msg = "您已经投过票,请勿重复投票!"
            else:
                login_staff.had_poll = True
                login_staff.save()
                checkedIds = request.POST.getlist("checkedId")
                for staff_id in checkedIds:
                    staff = Staff.objects.get(id=staff_id)
                    staff.poll_num += 1
                    staff.save()
                msg = "投票成功!"
    else:
        msg = "对不起，您没有投票权!"
    return render(request, "poll/best.html", locals())


@login_required
def staff(request):
    login_staff = Staff.objects.get(user=request.user)
    staffs = Staff.objects.filter(scored_right=True)
    evaluation = Evaluation.objects.all()[0]
    for staff in staffs:
        lst_record = StaffEvaluation.objects.filter(evaluation=evaluation, staff=staff, create_staff=login_staff)
        staff.lst_record = lst_record
    return render(request, "poll/staff.html", locals())


@login_required
def evaluation(request):
    login_staff = Staff.objects.get(user=request.user)
    if request.method == "GET":
        staff_id = request.GET.get("staff")
        staff = Staff.objects.get(id=staff_id)
        evaluation = Evaluation.objects.all()[0]
        lst_se = StaffEvaluation.objects.filter(evaluation=evaluation, staff=staff, create_staff=login_staff)
        if len(lst_se) > 0:
            msg = u"您已经给职工%s打过分!" % staff.name
        else:
            evaluationItems = EvaluationItems.objects.filter(evaluation=evaluation)
        return render(request, "poll/evaluation.html", locals())
    else:

        evaluation_id = request.POST.get("evaluation_id")
        staff_id = request.POST.get("staff_id")
        evaluation = Evaluation.objects.get(id=evaluation_id)
        staff = Staff.objects.get(id=staff_id)

        post_keys = request.POST.keys()
        item_and_point = []
        for key in post_keys:
            if str(key).startswith("evalue_"):
                item = Items.objects.get(id=int(key.replace("evalue_", "")))
                item_and_point.append([item, int(request.POST.get(key))])
        for item_point in item_and_point:
            st = StaffEvaluation(staff=staff, evaluation=evaluation,
                                 items=item_point[0], point=item_point[1], create_staff=login_staff)
            st.save()
        ses = StaffEvaluation.objects.filter(staff=staff, evaluation=evaluation)
        score, dafen = 0, []
        for se in ses:
            score = score + se.point
            dafen.append(se.create_staff.id)
        avg = float(score) / float(len(set(dafen)))
        staff.score = "%.2f" % avg
        staff.save()
        return redirect(reverse("poll_staff"))

