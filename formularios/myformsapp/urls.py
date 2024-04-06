from django.urls import path
from . import views

urlpatterns = [
    path('nueva-pagina/', views.nueva_pagina, name='nueva_pagina'),
]
