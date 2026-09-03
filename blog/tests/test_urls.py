from rest_framework.test import APIClient
from blog.views import *
from blog.models import *
from django.contrib.auth import get_user_model
import pytest
from django.urls import reverse,resolve

User = get_user_model()

@pytest.mark.django_db
def test_book_list_api_url_resolve():
    url = reverse('bookss-list')
    assert url == '/blog/api/books/'

    resolver = resolve('/blog/api/books/')
    assert resolver.func.view_class == BookListApiView

@pytest.mark.django_db
def test_book_viewsets_api_url():
    url = '/blog/viewset/book/'
    resolver = resolve(url)

    assert resolver.func.cls == BookViewSet

@pytest.mark.django_db
def test_book_list_api_url_get():
    author = Author.objects.create(name='arshia')
    Book.objects.create(title='T1',author=author)

    client = APIClient()
    url = reverse('book-list')
    response = client.get(url)

    assert response.status_code == 200
    assert isinstance(response.json(),list)
    assert response.json()[0]['title'] == 'T1'

@pytest.mark.django_db
def test_book_viewsets_url_authenticated():

    user = User.objects.create_user(phone='09922800302',first_name='arshia',last_name='tehrani',password='Test12345678/@')
    author = Author.objects.create(name='A')

    client = APIClient()
    client.force_authenticate(user=user)
    url = '/blog/viewset/book/'
    response = client.post(url,{'title':'T1','author':author.id},format='json')

    assert response.status_code == 201
    assert response.json()['title'] == 'T1'
    assert response.json()['author_name'] == author.name