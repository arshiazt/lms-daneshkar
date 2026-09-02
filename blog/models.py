from django.db import models

# Create your models here.


class Author(models.Model):

    name = models.CharField(max_length=128)

    class Meta:
        ordering = ("-name",)

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=128)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.book.title} by {self.rating} stars"


class Category(models.Model):

    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "-name",
        ]

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="products"
    )
    slug = models.SlugField(max_length=128, unique=True)
    price = models.PositiveIntegerField()

    class Meta:
        ordering = [
            "-price",
        ]

    def __str__(self):
        return str(self.price)
