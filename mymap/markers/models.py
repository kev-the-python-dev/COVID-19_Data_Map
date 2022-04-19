''' Markers models.'''

from django.contrib.gis.db.models import PointField
from django.db import models

class Marker(models.Model):
    '''a marker with name and location.'''
    name = models.CharField(max_length=255)
    location = PointField()

    def serialize(self):
        import json
        json_dict = {}
        json_dict['type'] = 'Feature'
        json_dict['properties'] = dict(name=self.name)
        json_dict['geometry'] = dict(type='Point', coordinates=list([self.long, self.lat]))
        return(json.dumps(json_dict))
