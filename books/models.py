from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator,MaxValueValidator
from users.models import CustomUser
# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    isbn = models.PositiveIntegerField(unique=True)
    image_book = models.ImageField(default='books_images/default_book_image.jpg',upload_to='media/books_images/')
    price = models.DecimalField(max_digits=6,decimal_places=2)
    publisher = models.CharField(max_length=50,blank=True,null=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'books_table'


class Author (models.Model):
    name = models.CharField(max_length=50)
    f_name = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author_table'


class BookAuthor(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default='deleted author')

    def __str__(self):
        return f"{self.book.title} {self.author.name}"

    def get_info(self):
        return f"{self.book.title} {self.author.name}"

    class Meta:
        db_table = 'book_author_table'


class BookReview (models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    comment = models.TextField()
    star_given = models.PositiveIntegerField(default=8, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.book.title

    class Meta:
        db_table = 'review_table'

