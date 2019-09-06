from django.urls import path
from . import views

app_name = 'world'
urlpatterns = [
        path('', views.index, name='index'),
        path('<int:shape_pk>', views.shape, name='shape'),
        path('polyline/', views.polylinem, name="polyline"),




]