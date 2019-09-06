from django.urls import path
from . import views

app_name = 'world'
urlpatterns = [
        path('', views.index, name='index'),
        path('v1/<int:shape_pk>', views.shape_v1, name='shape_v1'),
        path('v2/<int:shape_pk>', views.shape_v2, name='shape_v2'),
]
