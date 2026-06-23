from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='books.index'),
    path('create/', views.BookCreateView.as_view(), name='books.create'),
    path('edit/<int:pk>/', views.BookUpdateView.as_view(), name='books.edit'),
    path('delete/<int:pk>/', views.BookDeleteView.as_view(), name='books.delete'),
    path('show/<int:pk>/', views.BookDetailView.as_view(), name='books.show'),
    path('login/', views.LoginView.as_view(), name='books.login'),
    path('logout/', views.LogoutView.as_view(), name='books.logout'),
    path('signup/', views.SignupView.as_view(), name='books.signup'),
]
