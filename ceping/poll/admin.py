#coding=utf-8
from django.contrib import admin
from poll.models import EvaluationItems, Evaluation, StaffEvaluation, Category, Items

admin.autodiscover()

admin.site.register(Category)
admin.site.register(Items)
admin.site.register(Evaluation)
admin.site.register(EvaluationItems)
admin.site.register(StaffEvaluation)
