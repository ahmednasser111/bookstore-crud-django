from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import login, logout
from .models import Book
from .forms import BookForm, SignupForm, LoginForm


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(LoginRequiredMixin, DetailView):
    """Requires login."""
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj


class BookCreateView(LoginRequiredMixin, CreateView):
    """Requires login."""
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('books.index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Requires login + books.change_book permission."""
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('books.index')
    permission_required = 'books.change_book'


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Requires login + books.delete_book permission."""
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('books.index')
    permission_required = 'books.delete_book'


class SignupView(View):
    template_name = 'books/signup.html'

    def get(self, request):
        return render(request, self.template_name, {'form': SignupForm()})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books.index')
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'books/login.html'

    def get(self, request):
        return render(request, self.template_name, {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            next_url = request.GET.get('next') or reverse('books.index')
            return redirect(next_url)
        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('books.index')
