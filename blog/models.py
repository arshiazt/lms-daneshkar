from django.db import models

# Create your models here.

class Post(models.Model):

    name = models.CharField(max_length=100)
    blog = models.TextField()
    slug = models.SlugField(max_length=100,unique=True)
    price = models.IntegerField()
    price2 = models.PositiveBigIntegerField()
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='blog_image/',blank=True,null=True)
    txt = models.JSONField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Article(models.Model):

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
        ('archived','Archived')
    )
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default='draft',)

    def __str__(self):
        return f'{self.title} - {self.get_status_display}'