# coding=utf-8
__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/11/16'

from django.contrib.gis import admin
from models.taxonomy import *
from models.classification import Classification, AdditionalCharacteristic, AdditionalDescription

admin.site.register(Domain, admin.ModelAdmin)
admin.site.register(Kingdom, admin.ModelAdmin)
admin.site.register(Phylum, admin.ModelAdmin)
admin.site.register(Class, admin.ModelAdmin)
admin.site.register(Order, admin.ModelAdmin)
admin.site.register(Family, admin.ModelAdmin)
admin.site.register(Genus, admin.ModelAdmin)
admin.site.register(SubSpecies, admin.ModelAdmin)
admin.site.register(Species, admin.ModelAdmin)


class AdditionalCharacteristicInline(admin.TabularInline):
    model = AdditionalCharacteristic
    extra = 1


class AdditionalDescriptionInline(admin.TabularInline):
    model = AdditionalDescription
    extra = 1


class ClassificationAdmin(admin.ModelAdmin):
    inlines = [AdditionalCharacteristicInline, AdditionalDescriptionInline]
    filter_horizontal = ('habitats',)


admin.site.register(Classification, ClassificationAdmin)
