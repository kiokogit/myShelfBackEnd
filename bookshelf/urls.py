from django.urls import path;
from . import views

urlpatterns = [
    path('books/all/', views.getBooks, name='getbooks'),
    path('books/add/', views.addBook, name='addbook'),
    path('books/edit/<str:pk>/', views.editBook, name='editbook'),
    path('books/delete/<str:pk>/', views.delBook, name='deletebook'),
    
    path('comments/all/', views.getComments, name='getcomments'),
    path('comments/add/<str:pk>/', views.addComment, name='addcomment'),
    path('comments/delete/<str:pk>/', views.delComment, name='deletecomment'),
]