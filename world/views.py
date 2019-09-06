from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint
import json
from .models.postgis import Shape, Layer
from .models.mongo import Collection


def index(request):
    return HttpResponse("Hello GeoDjango")


def shape_v1(request, shape_pk):
    layers_set = Layer.objects.filter(shape_id=shape_pk)
    context = {'layers_set': layers_set,
               'name': layers_set[0].shape.name,
               'previous': str(shape_pk - 1),
               'next': str(shape_pk + 1),
               'shape_count': Shape.objects.count(),
               'shape_pk': shape_pk,
               }
    return render(request, 'world/shape_v1.html', context)


def shape_v2(request, shape_pk):
    layer_set = Collection.objects(primary_key=shape_pk)[0]
    result = {'type': "FeatureCollection"}
    features = []
    pprint(layer_set.geometries)
    for geom in layer_set.geometries:
        f = {'type': 'Feature'}
        f.update(geom.geometry)
        features.append(f)
    result['features'] = features
    context = {'features': json.dumps(result),
               'name': "",
               'previous': str(shape_pk - 1),
               'next': str(shape_pk + 1),
               'shape_count': Shape.objects.count(),
               'shape_pk': shape_pk,
               }
    return render(request, 'world/shape_v2.html', context)
