from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

app_name='blog'
urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('users/<str:username>/', UserPostListView.as_view(),name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
    path('post/create/', PostCreateView.as_view(),name='post-create'),
    path('about/', views.about,name='blog-about'),
]
