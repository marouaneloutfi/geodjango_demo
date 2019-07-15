from django.db.models.signals import post_save
from .models import Layer
from .models import Shape


@receiver(post_save, sender=Layer)
def add_fk_Layer(sender, layer, **kwargs):
    shape = Shape.objects.get(name=layer.name)
    if shape == None:
        shape = Shape(name = Layer.name)
        print(Layer.name)

    Layer.shape = shape
    Layer.save()




