from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'desc', 'rate', 'views']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter book title'}),
            'desc': forms.Textarea(attrs={'placeholder': 'Enter book description', 'rows': 4}),
            'rate': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '5'}),
            'views': forms.NumberInput(attrs={'min': '0'}),
        }
