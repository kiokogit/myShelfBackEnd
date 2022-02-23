from rest_framework.serializers import ModelSerializer

from .models import Book, Comment;

#serializers
class BookSerializer(ModelSerializer):
    class Meta:
        model=Book;
        fields='__all__';
        
class CommentSerializer(ModelSerializer):
    book=BookSerializer(many=False);
    class Meta:
        model=Comment;
        fields='__all__';