import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from blog.models import Post


@pytest.mark.django_db
def test_post_list():
    client = APIClient()
    url = reverse('post-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_post_detail():
    client = APIClient()
    user = User.objects.create_user(username='testuser', password='testpassword')
    post = Post.objects.create(title='Test Post', content='Test Content', author=user)
    url = reverse('post-detail', kwargs={'pk': post.pk})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_post_create_authenticated():
    client = APIClient()
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.force_authenticate(user=user)
    url = reverse('post-create')
    data = {'title': 'New Post', 'content': 'New Content'}
    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_create_unauthenticated():
    client = APIClient()
    url = reverse('post-create')
    data = {'title': 'New Post', 'content': 'New Content'}
    response = client.post(url, data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_post_update_authenticated():
    client = APIClient()
    user = User.objects.create_user(username='testuser', password='testpassword')
    post = Post.objects.create(title='Test Post', content='Test Content', author=user)
    client.force_authenticate(user=user)
    url = reverse('post-update', kwargs={'pk': post.pk})
    data = {'title': 'Updated Post', 'content': 'Updated Content'}
    response = client.put(url, data)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_post_update_unauthenticated():
    client = APIClient()
    user = User.objects.create_user(username='testuser', password='testpassword')
    post = Post.objects.create(title='Test Post', content='Test Content', author=user)
    url = reverse('post-update', kwargs={'pk': post.pk})
    data = {'title': 'Updated Post', 'content': 'Updated Content'}
    response = client.put(url, data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_post_delete_authenticated():
    client = APIClient()
    user = User.objects.create_user(username='testuser', password='testpassword')
    post = Post.objects.create(title='Test Post', content='Test Content', author=user)
    client.force_authenticate(user=user)
    url = reverse('post-delete', kwargs={'pk': post.pk})
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_post_delete_unauthenticated():
    client = APIClient()
    user = User.objects.create_user(username='testuser', password='testpassword')
    post = Post.objects.create(title='Test Post', content='Test Content', author=user)
    url = reverse('post-delete', kwargs={'pk': post.pk})
    response = client.delete(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
