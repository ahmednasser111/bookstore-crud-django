from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books.index'),
    path('create/', views.create, name='books.create'),
    path('edit/<int:id>/', views.edit, name='books.edit'),
    path('delete/<int:id>/', views.delete, name='books.delete'),
    path('show/<int:id>/', views.show, name='books.show'),
]