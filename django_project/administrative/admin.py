# coding=utf-8
__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/11/16'

from django.contrib.gis import admin
from models.country import Country

admin.site.register(Country, admin.ModelAdmin)
