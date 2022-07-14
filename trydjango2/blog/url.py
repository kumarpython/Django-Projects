from django.urls import path
from .views import ArticleListView,ArticleDetailView,ArticleCreateView,ArticleUpdateView,ArticleDeleteView

# namespace = 'blog'

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('<int:pk>/edit', ArticleUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='delete'),
    path('create/', ArticleCreateView.as_view(), name='create'),
]
