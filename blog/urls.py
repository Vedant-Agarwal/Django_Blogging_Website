from django.conf.urls import url
from .views import PostListView, PostDetailView
from django.contrib import admin
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    url('', PostListView.as_view(), name='blog-home'),
    url('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    url('post/new/', PostCreateView.as_view(), name='post-create'),
    url('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    url('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    url('about/', views.about, name='blog-about'),
]
