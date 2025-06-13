from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.complaint_list, name='complaint_list'),
    path('create/', views.complaint_create, name='complaint_create'),
    path('update/<int:pk>/', views.complaint_update, name='complaint_update'),
    path('delete/<int:pk>/', views.complaint_delete, name='complaint_delete'),
    path('signup/', views.signup_view, name='signup'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
