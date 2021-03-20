from django.urls import path
from .views import product_list_view,product_detail_view,product_update_view,product_delete_view,product_create_view

app_name='products'
urlpatterns = [
    path('', product_list_view, name='list'),
    path('<int:id>/', product_detail_view, name='detail'),
    path('<int:id>/update/', product_update_view, name='update'),
    path('<int:id>/delete/', product_delete_view, name='delete'),
    path('create/', product_create_view, name='create'),
]
