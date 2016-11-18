__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/11/16'

from django.conf import settings
from django.contrib.gis.db import models
from administrative.models.country import Country
from .taxonomy import *
from .description import Description


class Classification(models.Model):
    id = models.AutoField(primary_key=True)
    domain = models.ForeignKey(Domain)
    kingdom = models.ForeignKey(Kingdom)
    phylum = models.ForeignKey(Phylum)
    classis = models.ForeignKey(Class)
    order = models.ForeignKey(Order)
    family = models.ForeignKey(Family)
    genus = models.ForeignKey(Genus)
    subspecies = models.ForeignKey(SubSpecies, blank=True, null=True)
    species = models.ForeignKey(Species)

    habitats = models.ManyToManyField(Country)

    def __unicode__(self):
        return self.name_en


class AdditionalCharacteristic(Description):
    classification = models.ForeignKey(Classification)


class AdditionalDescription(Description):
    image = models.ImageField(
        upload_to='%s/classification/characteristic/' % settings.MEDIA_ROOT,
        blank=True,
        null=True)
    classification = models.ForeignKey(Classification)
