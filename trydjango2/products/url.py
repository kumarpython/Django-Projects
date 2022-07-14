from django.urls import path
from .views import product_detail_view,product_create_view,product_edit_view,product_delete_view,product_list_view

app_name = 'products'

urlpatterns = [
    path('', product_list_view, name='list'),
    path('<int:ID>/', product_detail_view, name='detail'),
    path('<int:ID>/edit', product_edit_view, name='edit'),
    path('<int:ID>/delete', product_delete_view, name='delete'),
    path('create/', product_create_view, name='create'),
]
