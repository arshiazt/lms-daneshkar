from rest_framework import serializers
from .models import *

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id','rating','comment']

class BookSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(source='review_set',many=True,read_only=True)
    author_name = serializers.CharField(source='author.name',read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(),write_only=True)

    class Meta:
        model = Book
        fields = ['id','title','author_name','author','reviews']