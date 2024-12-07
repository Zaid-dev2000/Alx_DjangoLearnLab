from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View a single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

]
