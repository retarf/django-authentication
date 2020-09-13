from django.urls import path

from . import views

namespace = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('change/<int:pk>/', views.change, name='change'),
    path('list/', views.list, name='list'),
]
