import os
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource
from django.db.models.signals import pre_save
from .models import Layer
from .models import Shape

layer_mapping = {
    'geom': 'MULTIPOLYGON',
}


shapes = []
data_dir = os.path.join(os.path.dirname(__file__) + '/data/')
for dir in range(1, 10):
    for file in os.listdir(data_dir + str(dir)):
        if file.endswith(".shp"):
            shapes.append(os.path.abspath(
                os.path.join(data_dir, str(dir), file)
            ))


def run(verbose=True):
    global i
    i = 1
    for shape in shapes:
        ds = DataSource(shape)
        global global_name
        global_name= ds[0].name
        lm = LayerMapping(Layer, shape, layer_mapping, transform=False)
        pre_save.connect(set_fk_shape, sender=Layer)
        lm.save()
        i += 1


def set_fk_shape(sender, instance, **kwargs):
    try:
        shapes = Shape.objects.filter(name=global_name)
        print(global_name)
        shape = shapes[0]
    except:
        shape = None
    if shape is None:
        shape = Shape(name=global_name, description="Test shapefile :" + str(i))
        shape.save()

    instance.shape_id = shape.pk
