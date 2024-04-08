from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Books,Author,BookAuthor,BookReview
# Register your models here.


# class BookAuthorModelAdmin(admin.ModelAdmin):
#     search_fields = ['book.title', 'author.name']
#     list_display = ['book.title','author.name','create_at']
#     list_filter = ['book.title', 'author.name','create_at']


class BookModelAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description','isbn']
    list_display = ['title','isbn']
    list_filter = ['create_at']


admin.site.register(BookAuthor)
admin.site.register(Books, BookModelAdmin)
admin.site.register(Author)
admin.site.register(BookReview)


