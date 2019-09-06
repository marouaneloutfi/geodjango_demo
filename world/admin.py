from django.contrib.gis import admin
from .models.postgis import Shape, Layer

admin.site.register(Shape)
admin.site.register(Layer, admin.OSMGeoAdmin)
