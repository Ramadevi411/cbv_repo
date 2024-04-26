from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Book
class BookListView(ListView):
    model = Book

class BookListView(ListView):
    model = Book
    template_name = 'testapp/books.html'
    context_object_name = 'books'
    
#starts
class BookListView2(ListView):
    model = Book
    template_name = 'testapp/books.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book

class BookCreateView(CreateView):
    model = Book
    fields = ('title', 'author', 'pages', 'price')

class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'

from django.urls import reverse_lazy
class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('listbooks')





# Create your views here.
