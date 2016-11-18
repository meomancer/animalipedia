__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/11/16'

from .description import TaxonomyDescription


class Species(TaxonomyDescription):
    def __unicode__(self):
        return self.name_english


class SubSpecies(TaxonomyDescription):
    def __unicode__(self):
        return self.name_english


class Genus(TaxonomyDescription):
    def __unicode__(self):
        return self.name_english


class Family(TaxonomyDescription):
    def __unicode__(self):
        return self.name_english


class Order(TaxonomyDescription):
    def __unicode__(self):
        return self.name_english


class Class(TaxonomyDescription):
    def __unicode__(self):
        return self.name_english


class Phylum(TaxonomyDescription):
    def __unicode__(self):
        return self.name_english


class Kingdom(TaxonomyDescription):
    def __unicode__(self):
        return self.name_english


class Domain(TaxonomyDescription):
    def __unicode__(self):
        return self.name_english
