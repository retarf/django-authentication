from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('<int:pk>/index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/change/', views.change, name='change'),
    path('list/', views.list, name='list'),
    path('<int:pk>/user_page/', views.user_page, name='user_page'),
    path('', views.login, name='login'),
]
