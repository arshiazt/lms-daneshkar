import pytest
from blog.models import *

@pytest.mark.django_db
def test_author_str():
    author = Author.objects.create(name='arshiazt')
    assert str(author) == 'arshiazt'

@pytest.mark.django_db
def test_book_str():
    author = Author.objects.create(name='ali')
    book = Book.objects.create(title='World War',author=author)
    assert str(book) == 'World War'

@pytest.mark.django_db
def test_review_str():
    author = Author.objects.create(name='amir')
    book = Book.objects.create(title='World War 2',author=author)
    review = Review.objects.create(book=book,rating=5.5,comment='Nice')
    assert "Review for World War 2 by 5.5 stars" in str(review)

@pytest.mark.django_db
def test_category_str_and_ordering():
    Category.objects.create(name='A',slug='a',description='hello a')
    Category.objects.create(name='B',slug='b',description='hello b')
    names = list(Category.objects.values_list('name',flat=True))
    assert names == ['B','A']

@pytest.mark.django_db
def test_product_str_and_ordering():
    category = Category.objects.create(name='C',slug='c',description='hello c')
    Product.objects.create(category=category,slug='cheap',price=20)
    Product.objects.create(category=category,slug='expensive',price=150)
    prices = list(Product.objects.values_list('price',flat=True))
    assert prices == [150,20]