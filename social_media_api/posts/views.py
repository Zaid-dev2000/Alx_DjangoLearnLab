from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters

class PostFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    content = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title', 'content']

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can edit or delete
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostFilter

    def perform_create(self, serializer):
        # Automatically set the author to the current user
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can edit or delete

    def perform_create(self, serializer):
        # Automatically set the author to the current user
        serializer.save(author=self.request.user)


