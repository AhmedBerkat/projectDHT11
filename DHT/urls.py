from django.urls import path
from . import views, api

urlpatterns = [
    path('', views.home),
    path("api",api.dhtser,name='json'),

]