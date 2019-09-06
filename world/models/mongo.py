from mongoengine import *


class Geometry(EmbeddedDocument):
    geometry = DynamicField()


class Collection(Document):
    primary_key = IntField()
    name = StringField(max_length=512)
    description = StringField(max_length=512)
    geometries = ListField(EmbeddedDocumentField(Geometry))
