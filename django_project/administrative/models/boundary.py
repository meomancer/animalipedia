# coding=utf-8
__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/11/16'

from django.contrib.gis.db import models


class Boundary(models.Model):
    """This is an abstract model that vectors can inherit from. e.g. country"""
    name = models.CharField(
        verbose_name='',
        help_text='',
        max_length=50,
        null=False,
        blank=False)

    polygon_geometry = models.MultiPolygonField(
        srid=4326)

    id = models.AutoField(
        primary_key=True)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        app_label = 'event_mapper'
