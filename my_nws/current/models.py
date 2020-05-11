from django.db import models

"""
I am using sessions to store this information now ... but this is what a database looks like in Django

class Configuration(models.Model):
    station_code = models.CharField(max_length=4)
    units = models.CharField(max_length=1)

    def __str__(self):
        return "station_code: "+self.station_code + " units: "+self.units

"""
