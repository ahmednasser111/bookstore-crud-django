from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Book, Category


class BookForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = Book
        fields = ['title', 'desc', 'rate', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter book title (10–50 chars)'}),
            'desc': forms.Textarea(attrs={'placeholder': 'Enter book description', 'rows': 4}),
            'rate': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '5'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if len(title) < 10:
            raise ValidationError('Title must be at least 10 characters.')
        if len(title) > 50:
            raise ValidationError('Title must be at most 50 characters.')
        return title


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Category name (min 2 chars)'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        if len(name) < 2:
            raise ValidationError('Category name must be at least 2 characters.')
        return name


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    pass
