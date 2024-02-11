from rest_framework import generics, permissions
from blog.models import Post
from blog.serializers import PostSerializer


class PostListAPIView(generics.ListAPIView):
    """
    Retrieves a list of all posts.

    Permissions:
    - AllowAny: Anyone can access this endpoint.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


class PostDetailAPIView(generics.RetrieveAPIView):
    """
    Retrieves details of a specific post.

    Permissions:
    - AllowAny: Anyone can access this endpoint.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


class PostCreateAPIView(generics.CreateAPIView):
    """
    Creates a new post.

    Permissions:
    - IsAuthenticated: Only authenticated users can create posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostUpdateAPIView(generics.UpdateAPIView):
    """
    Updates an existing post.

    Permissions:
    - IsAuthenticated: Only authenticated users can update posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostDeleteAPIView(generics.DestroyAPIView):
    """
    Deletes an existing post.

    Permissions:
    - IsAuthenticated: Only authenticated users can delete posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
