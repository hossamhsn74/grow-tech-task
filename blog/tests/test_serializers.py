import pytest
from django.contrib.auth.models import User
from blog.serializers import PostSerializer


@pytest.mark.django_db
class TestPostSerializer:
    def test_valid_data(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        data = {'title': 'Test Title', 'content': 'Test Content', 'author': user}
        serializer = PostSerializer(data=data)
        assert serializer.is_valid()

    def test_empty_title(self):
        data = {'title': '', 'content': 'Test Content', 'author': None}
        serializer = PostSerializer(data=data)
        assert not serializer.is_valid()
        assert 'title' in serializer.errors

    def test_empty_content(self):
        data = {'title': 'Test Title', 'content': '', 'author': None}
        serializer = PostSerializer(data=data)
        assert not serializer.is_valid()
        assert 'content' in serializer.errors

    def test_empty_title_and_content(self):
        data = {'title': '', 'content': '', 'author': None}
        serializer = PostSerializer(data=data)
        assert not serializer.is_valid()
        assert 'title' in serializer.errors
        assert 'content' in serializer.errors

    def test_missing_title_and_content(self):
        data = {'author': None}  # Only author provided, title and content missing
        serializer = PostSerializer(data=data)
        assert not serializer.is_valid()
        assert 'title' in serializer.errors
        assert 'content' in serializer.errors
