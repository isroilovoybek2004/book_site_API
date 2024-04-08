from django.shortcuts import render
from django.views.generic import ListView,DetailView,View
from .models import Books
# Create your views here.


class BookList(View):
    def get(self,request):
        books = Books.objects.order_by('create_at')
        context = {
            'books': books
        }
        return render(request,'book/book_list.html', context=context)


class BookDetailView(View):
    def get(self, request,pk):
        book = Books.objects.get(pk=pk)
        context = {
            'book': book
        }
        return render(request, 'book/book_detail.html', context=context)