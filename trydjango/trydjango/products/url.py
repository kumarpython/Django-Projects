from django.urls import path
from products.views import product_detail_view,product_create_view,product_delete_view,product_all


app_name='products'
urlpatterns = [
    path('', product_all,name='products'),
    path('<int:id>/', product_detail_view,name='products-detail'),
    path('<int:id>/delete/', product_delete_view,name='products-delete'),
    path('create/', product_create_view,name='products-create'),

]