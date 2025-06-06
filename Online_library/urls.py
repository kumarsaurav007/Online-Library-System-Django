from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('authors/add/', AuthorCreateView.as_view(), name='add_author'),
    path('books/add/', BookCreateView.as_view(), name='add_book'),
    path('borrow/add/', BorrowRecordCreateView.as_view(), name='add_borrow'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('borrow/', BorrowListView.as_view(), name='borrow_list'),
    path('export/', ExportExcelView.as_view(), name='export_excel'),
]

