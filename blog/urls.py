from django.urls import path
from blog.views import PostListAPIView, PostDetailAPIView, PostCreateAPIView, PostUpdateAPIView, PostDeleteAPIView

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('posts/create/', PostCreateAPIView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/',
         PostUpdateAPIView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/',
         PostDeleteAPIView.as_view(), name='post-delete'),

]
