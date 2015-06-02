#coding=utf-8
from django.contrib import admin
from officesupply.models import Material, UseRecord

admin.autodiscover()

admin.site.register(Material)
admin.site.register(UseRecord)