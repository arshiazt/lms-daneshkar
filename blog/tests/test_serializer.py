import pytest
from blog.serializers import *
from blog.models import *

@pytest.mark.django_db
def test_review_serializer_output():

    book = Book.objects.create(title='t1',author=Author.objects.create(name='ali'))
    review = Review.objects.create(book=book,rating=3,comment='Nice')

    serializer = ReviewSerializer(instance=review)
    data = serializer.data

    assert data['id'] == review.id
    assert data['rating'] == 3
    assert data['comment'] == 'Nice'

@pytest.mark.django_db
def test_review_nested_serializer_output():

    author = Author.objects.create(name='reza')
    book = Book.objects.create(title='T1',author=author)
    review = Review.objects.create(book=book,rating=4,comment='Nice')
    review = Review.objects.create(book=book,rating=3,comment='Bad')

    serializer = BookSerializer(instance=book)
    data = serializer.data
    
    assert data['id'] == book.id
    assert data['title'] == 'T1'
    assert data['author_name'] == 'reza'
    assert 'aouthor' not in data
    assert len(data['reviews']) == 2
    assert data['reviews'][0]['rating'] == 4
    assert data['reviews'][0]['comment'] == 'Nice'

@pytest.mark.django_db
def test_review_serializer_validated_data():

    author = Author.objects.create(name='reza')
    valid_data ={
        'title':'New',
        'author':author.id
    }
    serializer = BookSerializer(data=valid_data)

    assert serializer.is_valid(),serializer.errors

    book = serializer.save()
    assert book.title == 'New'
    assert book.author == author

@pytest.mark.django_db
def test_review_serializer_invalidated_data():

    invalid_data = {
        'title':'',
        'author':None
    }
    serializer = BookSerializer(data=invalid_data)
    assert not serializer.is_valid()
    assert 'title' in serializer.errors
    assert 'author' in serializer.errors