from django.forms import ModelForm;
from .models import Book, Comment;

#forms to save data
#book form
class BookForm(ModelForm):
    class Meta:
        model=Book;
        fields='__all__';

#comments form
class CommentForm(ModelForm):
    class Meta:
        model=Comment;
        fields='__all__';