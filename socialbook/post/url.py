from django.urls import path
from .views import list,detail,edit,delete

app_name='post'

urlpatterns = [
    path('',list,name='home'),
    path('<int:id>/',detail,name='detail'),
    path('<int:id>/edit/',edit,name='edit'),
    path('<int:id>/delete/',delete,name='delete'),
]
