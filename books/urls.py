from django.urls import path
from .views import BookList,BookDetailView
app_name = 'books'
urlpatterns = [
    path('', BookList.as_view(),name='book-list'),
    path('book-detail', BookDetailView.as_view(),name='book-detail')
]