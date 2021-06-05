from django.urls import path
from .views import *

urlpatterns = [
    path('',indexview),
    path('logoutuser/',logoutuser,name = 'logoutuser'),

    
]