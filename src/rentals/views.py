from django.views.generic import (
    ListView, 
)
from django.shortcuts import redirect, render
from django.db.models import Q
from books.models import Book

from rentals.forms import SearchBookForm
from rentals.models import Rental

# Create your views here.

def search_book_view(request):
    form = SearchBookForm(request.POST or None)
    search_query = request.POST.get('search', None)
    book_ex = Book.objects.filter(isbn=search_query).exists()

    if search_query is not None and book_ex:
        return redirect('rentals:detail', search_query)
    
    context = {
        'form': form,
    }
    return render(request, 'rentals/main.html', context)

class BookRentalHistoryView(ListView):
    model = Rental # Rental.objects.all()
    template_name = 'rentals/detail.html'

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        return Rental.objects.filter(book__isbn=book_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = self.get_queryset()
        obj = None
        if qs.exists():
            obj = qs.first()
        context['obj'] = obj
        return context
    