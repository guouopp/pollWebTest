#coding=utf-8

from django.db import models
from staff.models import Staff


class Material(models.Model):
    name = models.CharField(verbose_name="办公用品名称", max_length=100, null=False, blank=False)
    stock = models.SmallIntegerField(verbose_name="库存", null=False, blank=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "办公用品"
        verbose_name_plural = "办公用品管理"


class UseRecord(models.Model):
    material = models.ForeignKey(Material, verbose_name="办公用品")
    staff = models.ForeignKey(Staff, verbose_name="员工")
    number = models.SmallIntegerField(verbose_name="领用数量", null=False, blank=False)
    use_date = models.DateTimeField(verbose_name="领用时间", null=False, blank=False, auto_now_add=True)

    def __unicode__(self):
        return "%s:%s:%s:%s" % (self.material.name, self.staff.name, self.number, self.use_date)

    class Meta:
        verbose_name = "领用记录"
        verbose_name_plural = "领用记录管理"

