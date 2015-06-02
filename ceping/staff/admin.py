# coding=utf-8
from django.contrib import admin
from staff.models import Staff

admin.autodiscover()


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'poll_right', 'vote_right', "had_poll", "poll_num",
                    "score_right", "scored_right", "score")
    actions = [
        'update_poll_right_true', 'update_poll_right_false',
        "update_vote_right_true", "update_vote_right_false",
        "update_score_right_true", "update_score_right_false",
        "update_scored_right_true", "update_scored_right_false"
    ]

    def update_poll_right_true(self, request, queryset):
        queryset.update(poll_right=True)
    update_poll_right_true.short_description = "启用投票权"

    def update_poll_right_false(self, request, queryset):
        queryset.update(poll_right=False)
    update_poll_right_false.short_description = "禁用投票权"

    def update_vote_right_true(self, request, queryset):
        queryset.update(vote_right=True)
    update_vote_right_true.short_description = "启用被选举权"

    def update_vote_right_false(self, request, queryset):
        queryset.update(vote_right=False)
    update_vote_right_false.short_description = "禁用被选举权"

    def update_score_right_true(self, request, queryset):
        queryset.update(score_right=True)
    update_score_right_true.short_description = "启用打分权"

    def update_score_right_false(self, request, queryset):
        queryset.update(score_right=False)
    update_score_right_false.short_description = "禁用打分权"

    def update_scored_right_true(self, request, queryset):
        queryset.update(scored_right=True)
    update_scored_right_true.short_description = "启用被打分权"

    def update_scored_right_false(self, request, queryset):
        queryset.update(scored_right=False)
    update_scored_right_false.short_description = "禁用被打分权"




admin.site.register(Staff, StaffAdmin)