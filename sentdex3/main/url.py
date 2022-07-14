from django.urls import path, include
from .views import homepage,register,logout_user,login_user,ss

app_name='main'

urlpatterns = [
    path('', homepage,name='homepage'),
    path('register', register,name='register'),
    path('tinymce/', include('tinymce.urls')),
    path('logout/', logout_user,name='logout'),
    path('login/', login_user,name='login'),
    path('<int:ss>/', ss,name='ss'),

]