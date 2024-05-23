from django.urls import path
from . import views
from .views import index , details 

urlpatterns = [
    path('', views.index, name='index'), 
    path('details', views.details, name='details'),  
]