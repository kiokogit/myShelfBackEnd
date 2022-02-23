from tabnanny import verbose
from django.db import models

#Create your models here.
#book model
class Book(models.Model):
    #primary details
    title=models.CharField(verbose_name='title', max_length=200);
    author=models.CharField(max_length=200);
    pages=models.IntegerField();
    cover=models.TextField(null=True, blank=True);
    format=models.CharField(max_length=200)
    #defaults
    date_added=models.DateTimeField(auto_now_add=True);
    #reading
    reading_complete=models.BooleanField(default=False);
    reading_ongoing=models.BooleanField(default=False);
    reading_progress=models.IntegerField(default=0, null=True, blank=True);
    last_reading=models.DateTimeField(null=True, blank=True);
    reading_closed=models.BooleanField(default=False);
    #rating/reviews
    liked=models.BooleanField(default=False); #if liked, disable dislike button
    disliked=models.BooleanField(default=False);
    rating=models.JSONField(null=True, blank=True);  #has date liked, and rating number
    average_rating=models.IntegerField(null=True, blank=True);    
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE);
    date=models.DateTimeField(auto_now_add=True);
    body=models.TextField(); #cannot be blank
    
    def __str__(self):
        return self.body[:50];
