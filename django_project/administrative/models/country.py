# coding=utf-8
"""Docstring for this file."""
__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/11/16'

from .boundary import Boundary


class Country(Boundary):
    """Class for Country."""

    class Meta:
        """Meta Class"""
        verbose_name_plural = 'Countries'


Country._meta.get_field('name').verbose_name = 'Country name'
Country._meta.get_field('name').help_text = 'The name of the country.'
