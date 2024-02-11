import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from blog.models import Post


@pytest.mark.django_db
class TestPostModel:
    def test_create_post(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        title = 'Test Title'
        content = 'Test Content'
        post = Post.objects.create(title=title, content=content, author=user)

        assert post.title == title
        assert post.content == content
        assert post.author == user
        assert post.published_on is not None

    def test_str_representation(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        title = 'Test Title'
        post = Post.objects.create(title=title, content='Test Content', author=user)

        assert str(post) == title

    def test_ordering(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        post1 = Post.objects.create(title='Post 1', content='Content 1', author=user, published_on=timezone.now())
        post2 = Post.objects.create(title='Post 2', content='Content 2', author=user, published_on=timezone.now())

        posts = Post.objects.all()
        assert posts[0] == post2
        assert posts[1] == post1
