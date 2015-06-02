#coding=utf-8
from django.contrib.auth.models import User
from django.db import models
from staff.models import Staff


class Category(models.Model):
    name = models.CharField(verbose_name="题库类别", max_length=200, null=False, blank=False)

    def  __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = '题库类别'
        verbose_name_plural = "题库类别管理"


class Items(models.Model):
    category = models.ForeignKey(Category, verbose_name="所属题库类别")
    name = models.CharField(verbose_name="题目", max_length=1000, null=False, blank=False)
    point = models.SmallIntegerField(verbose_name="分值", null=False, blank=False)

    def __unicode__(self):
        return u"%s:%s" % (self.name, self.point)

    class Meta:
        verbose_name = '题目'
        verbose_name_plural = "题目管理"


class Evaluation(models.Model):
    name = models.CharField(verbose_name="测评表名称", max_length=200, null=False, blank=False)
    is_used = models.BooleanField(verbose_name="是否启用", default=True)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = '测评表'
        verbose_name_plural = "测评表管理"


class EvaluationItems(models.Model):
    evaluation = models.ForeignKey(Evaluation, verbose_name='测评表')
    items = models.ForeignKey(Items, verbose_name='题目')

    def __unicode__(self):
        return u"%s:%s" % (self.evaluation.name, self.items.name)

    class Meta:
        verbose_name = '测评表题目'
        verbose_name_plural = "测评表题目管理"


class StaffEvaluation(models.Model):
    #被打分人
    staff = models.ForeignKey(Staff, verbose_name='员工', related_name="evaluation_staff")
    evaluation = models.ForeignKey(Evaluation, verbose_name='测评表')
    items = models.ForeignKey(Items, verbose_name='题目')
    point = models.SmallIntegerField(verbose_name="分值", null=False, blank=False)
    #打分人
    create_staff = models.ForeignKey(Staff, verbose_name='打分员工', related_name="create_staff")

    def __unicode__(self):
        return u"%s:%s:%s:%s" % (self.staff.name, self.evaluation.name, self.items.name, self.point)

    class Meta:
        verbose_name = '员工评分'
        verbose_name_plural = "员工评分管理"
