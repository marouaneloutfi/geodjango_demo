from django.shortcuts import render
from django.http import HttpResponse
import geopandas
import json
from .models import Layer
from .models import Shape
from .measurements import zip_geometry


def index(request):
    return HttpResponse("Hello GeoDjango")


def shape(request, shape_pk):
    layers_set = Layer.objects.filter(shape_id=shape_pk)
    context = {'layers_set': layers_set,
               'name': layers_set[0].shape.name,
               'previous': str(shape_pk - 1),
               'next': str(shape_pk + 1),
               'shape_count': Shape.objects.count(),
               'shape_pk': shape_pk,
               }
    return render(request, 'world/shape.html', context)


def polylinem(request):

    gdf = geopandas.read_file('/home/marouane/stage/testdata/polylineM/asv_lines_Calibrated.shp')
    i = 0
    measurements = {'type': "FeatureCollection"}
    features = []
    for f in gdf.iterfeatures():
        if i == 132:
            features.append({'type': 'Feature', 'geometry': zip_geometry(f['geometry'], f['properties']['measurements'])})
            measurements['features'] = features
        i += 1
    context = {
        'features': json.dumps(measurements)
    }
    return render(request, 'world/measurements.html', context)
