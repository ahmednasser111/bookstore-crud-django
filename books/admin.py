from django.contrib import admin
from .models import Book, Category, ISBN


class ISBNInline(admin.StackedInline):
    """Stacked inline: shows ISBN details inside Book admin page."""
    model = ISBN
    extra = 0
    can_delete = False
    readonly_fields = ('isbn_number',)
    fields = ('author_title', 'book_title', 'isbn_number')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'rate', 'views', 'get_categories')
    list_filter = ('categories', 'user', 'rate')
    search_fields = ('title', 'desc', 'user__username')
    ordering = ('-views',)
    filter_horizontal = ('categories',)
    inlines = [ISBNInline]

    def get_categories(self, obj):
        return ', '.join(c.name for c in obj.categories.all())
    get_categories.short_description = 'Categories'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'book_count')
    search_fields = ('name',)

    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Books'


@admin.register(ISBN)
class ISBNAdmin(admin.ModelAdmin):
    list_display = ('isbn_number', 'book_title', 'author_title', 'book')
    search_fields = ('isbn_number', 'book_title', 'author_title')
    readonly_fields = ('isbn_number',)
    list_filter = ('book__categories',)
