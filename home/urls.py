
from django.urls import path, include

from django.contrib.auth.views import LogoutView
from . import views
from .views import ResetPasswordView
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', views.home, name='home'),
   
    path('home/', views.home, name='home'),
    path('chart/', views.home_chart, name='home_chart'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('profile/', views.userprofile, name='userprofile'),
    path('add_profile/<int:id>/', views.add_profile, name='add_profile'),
    path('user_profile/', views.user_profile, name='user_profile'),
   
    path('activity_filter/', views.activity_filter, name='activity_filter'),
    path('user_activity/', views.user_activity, name='user_activity'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
   
    path('change_password/', views.change_password, name='change_password'),
    path('change_success/', views.change_success, name='change_success'),
]
  
  

