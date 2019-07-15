from django.shortcuts import render
from django.http import HttpResponse
from .models import Layer
from .models import Shape


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
