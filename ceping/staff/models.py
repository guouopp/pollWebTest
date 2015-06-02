#coding=utf-8
from django.contrib.auth.models import User

from django.db import models


class Staff(models.Model):
    user = models.OneToOneField(User, verbose_name="用户ID")
    name = models.CharField(verbose_name="员工姓名", max_length=20, null=False, blank=False)
    poll_right = models.BooleanField(verbose_name="投票权？", default=True, null=False, blank=False)
    vote_right = models.BooleanField(verbose_name="被选举权？", default=True, null=False, blank=False)
    had_poll = models.BooleanField(verbose_name="是否已投票", default=False, null=False, blank=False)
    poll_num = models.SmallIntegerField(verbose_name="得票数", default=0, null=True, blank=True)
    score_right = models.BooleanField(verbose_name="评分权？", default=True, null=False, blank=False)
    scored_right = models.BooleanField(verbose_name="被评分权？", default=True, null=False, blank=False)
    score = models.FloatField(verbose_name="平均分", default=0.00, null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = '员工'
        verbose_name_plural = "员工管理"
