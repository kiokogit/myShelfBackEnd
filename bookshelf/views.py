from datetime import datetime
from django.shortcuts import render;

from rest_framework.decorators import api_view;
from rest_framework.response import Response;

from .forms import BookForm, CommentForm;
from .serializers import BookSerializer, CommentSerializer;
from .models import Book, Comment;

# Create your views here.

#get all books
@api_view(['GET'])
def getBooks(request):    
    books = Book.objects.all() #try and order by
    serialized = BookSerializer(books, many=True);
    return Response(status=200, data=serialized.data);

#add a book to shelf
@api_view(['POST'])
def addBook(request):
    
    data = request.data;
    form = BookForm(data);
    if form.is_valid():
        form.save(commit=True);
        return Response(status=200);
    
    else:
        print(form.errors.as_json());
        return Response(status=500);
    
@api_view(['DELETE'])
def delBook(request, pk):
    book = Book.objects.get(id=pk);
    book.delete();
    
    return Response(status=200);

@api_view(['PATCH'])
def editBook(request, pk):
    #send data by body - this includes like, update reading progress, or edit other details
    data=request.data;
    book = Book.objects.get(id=pk);
    form=BookForm(data, instance=book);
    if form.is_valid():
        form.save(commit=True);
        return Response(status=201);
    else:
        print(form.errors.as_json());
        return Response(status=500);

#get comments
@api_view(['GET'])
def getComments(request):
    comments=Comment.objects.all();
    serialized = CommentSerializer(comments, many=True);
    return Response(status=200, data=serialized.data);

#add comments
@api_view(['POST'])
def addComment(request, pk):        #the comment has a book instance, sent as parameter key pk
    data=request.data;
    book = Book.objects.get(id=pk);
    #get book, and fetch body from the data sent; Client sends comment body only; date/time is auto_add now
    comment = {'book':book, 'body':data['body']}
    print(comment)
    form = CommentForm(comment);
    
    if form.is_valid():
        comment = form.save(commit=True);
        return Response(status=201);
    else:
        print(form.errors.as_json());
        return Response(status=500);

#delete comments
@api_view(['DELETE'])
def delComment(request, pk):
    comment=Comment.objects.get(id=pk);
    comment.delete();
    return Response(200);