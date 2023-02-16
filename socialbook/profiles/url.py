from django.urls import path
from .views import register,login_user,logout_user,create_profile,profile,edit_profile,friends

app_name='profiles'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create/', create_profile, name='create'),
    path('<int:id>/', profile, name='profile'),
    path('<int:id>/edit/', edit_profile, name='edit'),
    path('<int:id>/friends/', friends, name='friends'),

]
