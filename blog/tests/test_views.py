import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from blog.models import *
from django.contrib.auth import get_user_model

User = get_user_model()
# @pytest.mark.django_db
# def test_test_view_get(client):
#     url = reverse('test')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert 'text/html' in response['Content-Type']

# @pytest.mark.django_db
# def test_test_view_get_renders_template(client):
#     url = reverse('test')
#     response = client.get(url)
#     assert 'test.html' in {t.name for t in response.templates}

# @pytest.mark.django_db
# def test_test_view_post(client):
#     url = reverse('test')
#     data = {
#         'name':'arshia',
#         'message':'hello'
#     }
#     response = client.post(url,data)
#     assert response.status_code == 200
#     assert 'arshia hello' 

@pytest.mark.django_db
def test_book_list_view():

    author = Author.objects.create(name='arshiazt')
    book = Book.objects.create(title='world war',author=author)
    Review.objects.create(book=book,rating=5,comment='Nice')
    Review.objects.create(book=book,rating=3,comment='not bad')

    client = APIClient()
    url = reverse('book-list')
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['title'] == 'world war'
    assert len(response.data[0]['reviews']) == 2

@pytest.mark.django_db
def test_book_list_statu_code_get():

    client = APIClient()
    url = reverse('book-list')
    response = client.get(url)
    
    assert response.status_code == 200

@pytest.mark.django_db
def test_book_list_statu_code_not_found():

    client = APIClient()
    url = reverse('book-list',args=[999])
    response = client.get(url)

    assert response.status_code == 404

@pytest.mark.django_db
def test_book_list_statu_return_data():

    author = Author.objects.create(name='arshiazt')
    book = Book.objects.create(title='world war',author=author)

    client = APIClient()
    response = client.get(reverse('book-list'))

    assert response.status_code == 200
    assert isinstance(response.data,list)
    assert 'title' in response.data[0]

@pytest.mark.django_db
def test_book_list_filter():

    author1 = Author.objects.create(name='author1')
    author2 = Author.objects.create(name='author2')
    Book.objects.create(title='title1',author=author1)
    Book.objects.create(title='title2',author=author2)
    
    client = APIClient()
    url = reverse('book-list') + f'?author={author1.id}'
    response = client.get(url)

    assert response.status_code == 200
    assert all(book['title'] == 'title1' for book in response.data)

@pytest.mark.django_db
def test_book_list_order():

    a = Author.objects.create(name='A')
    Book.objects.create(title='title1',author=a)
    Book.objects.create(title='title2',author=a)

    client = APIClient()
    url = reverse('book-list') + '?ordering=title'
    response = client.get(url)

    assert response.data[0]['title'] == 'title1'

@pytest.mark.django_db
def test_book_list_not_authenticated():

    client = APIClient()
    data = {'title':'book123','author':1}
    response = client.post(reverse('book-list'),data)

    assert response.status_code == 403 or response.status_code == 401

@pytest.mark.django_db
def test_book_list_authenticated():

    user = User.objects.create_user(phone='09922800302',first_name='arshia',last_name='tehrani',password='Test12345678/@')
    author = Author.objects.create(name='A')

    client = APIClient()
    client.force_authenticate(user=user)
    response = client.post(reverse('book-list'),{'title':'book1','author':author.id})

    assert response.status_code == 201