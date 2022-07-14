from django.urls import path
from .views import register,profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register,name='register'),
    path('reset/', auth_views.PasswordResetView.as_view(template_name='users/reset.html'),name='reset'),
    path('reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='users/reset_done.html'),name='reset-done'),
    path('reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/reset_confirm.html'),name='reset-confirm'),
    path('reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/reset_complete.html'),name='reset-complete'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/', profile,name='profile'),

]