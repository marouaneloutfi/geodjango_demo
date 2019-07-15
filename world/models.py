from django.contrib.gis.db import models


class Shape(models.Model):
    name = models.CharField(max_length=512)
    description = models.CharField(max_length=512)


class Layer(models.Model):
    geom = models.MultiPolygonField(srid=4326)
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE)
