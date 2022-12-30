from django.urls import path
from app2.views import *
app_name='pasupathi'

urlpatterns=[
    path('pasupathi/',pasupathi,name='pasupathi'),
]