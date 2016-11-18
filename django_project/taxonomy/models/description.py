__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/11/16'

from django.contrib.gis.db import models



class Description(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class TaxonomyDescription(models.Model):
    id = models.AutoField(primary_key=True)
    name_latin = models.CharField(max_length=128)
    name_english = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name_latin

    class Meta:
        abstract = True
