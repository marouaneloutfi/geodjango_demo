from django.contrib.gis import admin
from .models import Layer
from .models import Shape


admin.site.register(Shape)
admin.site.register(Layer, admin.OSMGeoAdmin)
