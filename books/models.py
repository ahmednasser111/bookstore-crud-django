import random
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError


def validate_book_title(value):
    if len(value) < 10:
        raise ValidationError('Book title must be at least 10 characters.')
    if len(value) > 50:
        raise ValidationError('Book title must be at most 50 characters.')


class Category(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50, validators=[validate_book_title])
    desc = models.TextField(default='')
    rate = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    views = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    categories = models.ManyToManyField(Category, related_name='books')

    def __str__(self):
        return self.title


class ISBN(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='isbn')
    author_title = models.CharField(max_length=200, blank=True)
    book_title = models.CharField(max_length=50)
    isbn_number = models.CharField(max_length=13, unique=True, blank=True)

    class Meta:
        verbose_name = 'ISBN'
        verbose_name_plural = 'ISBNs'

    def save(self, *args, **kwargs):
        if not self.isbn_number:
            self.isbn_number = self._generate_isbn()
        super().save(*args, **kwargs)

    def _generate_isbn(self):
        prefix = '978'
        digits = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        base = prefix + digits
        total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(base))
        check = (10 - (total % 10)) % 10
        return base + str(check)

    def __str__(self):
        return f'{self.isbn_number} — {self.book_title}'
