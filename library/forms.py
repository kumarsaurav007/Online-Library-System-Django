
from django import forms
from .models import Author, Book, BorrowRecord

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio']


class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['user_name', 'book', 'borrow_date', 'return_date']

class BookForm(forms.ModelForm):
    author_name = forms.CharField(label='Author Name')

    class Meta:
        model = Book
        fields = ['title', 'genre', 'published_date']  # NOT including 'author'

    def clean_author_name(self):
        name = self.cleaned_data['author_name'].strip()
        author, _ = Author.objects.get_or_create(name=name)
        return author

    def save(self, commit=True):
        book = super().save(commit=False)
        book.author = self.cleaned_data['author_name']
        if commit:
            book.save()
        return book