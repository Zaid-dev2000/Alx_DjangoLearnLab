from rest_framework import viewsets, permissions, status, generics
from .models import Post, Comment, Post, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.response import Response
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

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

        class FeedView(permissions.IsAuthenticated):
            permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # Get posts from users the current user is following, ordered by created_at
        followed_users = user.following.all()
        posts = ["Post.objects.filter(author__in=following_users).order_by"]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Use get_object_or_404 to get the post by pk or return a 404 error
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user

        # Use get_or_create to avoid duplicate likes from the same user
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({'detail': 'You already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification for the post author
        notification = Notification.objects.create(
            recipient=post.author,  # Post author receives the notification
            actor=user,
            verb="liked your post",
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=post.id
        )

        return Response({'detail': 'Post liked successfully'}, status=status.HTTP_200_OK)


class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Use get_object_or_404 to get the post by pk or return a 404 error
        post = generics.et_object_or_404(Post, pk=pk)
        user = request.user

        # Use get_object_or_404 to check if the Like exists
        like = get_object_or_404(Like, user=user, post=post)

        # Remove the like
        like.delete()

        return Response({'detail': 'Post unliked successfully'}, status=status.HTTP_200_OK)


