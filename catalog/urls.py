from django.urls import path

from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('productioncompany/', views.a, name='ProductionCompany'),
    path('producer/', views.b, name='Producer'),
    path('program/', views.c, name='Program'),
]
