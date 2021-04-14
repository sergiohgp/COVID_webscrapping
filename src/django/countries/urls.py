from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.country_list, name='countries'),
    path('country/edit/<str:id>/', views.country_edit, name='edit'),
    path('country/add/', views.country_add, name='add'),
    path('insert/', views.country_insert, name='insert'),
    path('update/', views.country_update, name='update'),
    path('delete/<str:id>/', views.country_delete, name='delete'),
]
