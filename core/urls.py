from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('example/', example),
    path('chart2/', chart2),
    path('chart3/', chart3),
    path('chart4/', chart4),
    path('chart5/', chart5),
    path('chart6/', chart6)
]
