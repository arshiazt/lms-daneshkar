import factory
from blog.models import *

class AuthorFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Author
    name = 'Test Author'

class BookFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Book
    title = factory.sequence(lambda n: f'Book {n}')
    author = factory.SubFactory(AuthorFactory)