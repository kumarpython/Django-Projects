from django.urls import path
from blogs.views import (ArticleListView,ArticleDetailView,ArticleCreateView,ArticleUpdateView,ArticleDeleteView)


app_name='blogs'
urlpatterns = [
    path('', ArticleListView.as_view(),name='blogs'),
    path('<int:id>/', ArticleDetailView.as_view(),name=''),
    path('create/', ArticleCreateView.as_view(),name='blogs-create'),
    path('<int:id>/update/', ArticleUpdateView.as_view(),name='blogs-update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(),name='blogs-delete'),
    # path('<int:id>/update/', product_detail_view,name='blogs-update'),
    # path('<int:id>/delete/', product_delete_view,name='blogs-delete'),
    # path('create/', product_create_view,name='blogs-create'),

]