from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView, PostByTagListView

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/new/', views.post_create, name='post-create'),
    path('post/<int:pk>/update/', views.post_update, name='post-update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post-delete'),

    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),  # Filter posts by tag

    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),  # Add a new comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit-comment'),  # Edit a comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),

    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
