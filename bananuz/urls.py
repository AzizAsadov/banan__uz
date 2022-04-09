from django.urls import path, include
from .views import *

urlpatterns = [
    path('base/' ,  base , name='base'),
    path('' ,  home , name='home'),
    path('category/<slug:slug>' ,  category , name='category'),
    path('province/<slug:slug>' ,  province , name='province'),
]