from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
    path('add/', views.add_gift, name='add_gift'),
    path('edit/<int:pk>/', views.edit_gift, name='edit_gift'),
    path('delete/<int:pk>/', views.delete_gift, name='delete_gift'),

]
