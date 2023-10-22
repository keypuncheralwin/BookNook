from datetime import datetime
from django.urls import reverse
from django.views.generic import (
    ListView, UpdateView, CreateView, FormView
)
from django.contrib import messages
from django.shortcuts import redirect, render
from django.db.models import Q
from django.http import HttpResponse

from books.models import Book
from rentals.admin import RentalResource
from rentals.choices import FORMAT_CHOICES
# from . admin import RentalResource
from rentals.forms import SearchBookForm, SelectExportOptionForm
from rentals.models import Rental

# Create your views here.

def search_book_view(request):
    form = SearchBookForm(request.POST or None)
    search_query = request.POST.get('search', None)
    book_ex = Book.objects.filter(Q(isbn=search_query) | Q(id=search_query)).exists()

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
        return Rental.objects.filter(Q(book__isbn=book_id) | Q(book__id=book_id))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = self.kwargs.get('book_id')
        obj = Book.objects.filter(Q(isbn=book_id) | Q(id=book_id)).first()
        context['object'] = obj
        context['book_id'] = book_id
        return context
    
class UpdateRentalStatusView(UpdateView):
    model = Rental
    template_name = 'rentals/update.html'
    fields = ("status",)

    def get_success_url(self):
        book_id = self.kwargs.get('book_id')
        return reverse('rentals:detail', kwargs={'book_id':book_id})
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        if instance.status == '#1':
            instance.return_date = datetime.today().date()
            instance.is_closed = True
        instance.save()
        messages.add_message(self.request, messages.INFO, f"{instance.book.id} was successfuly updated")
        return super().form_valid(form)
    
class CreateNewRentalView(CreateView):
    model = Rental
    template_name = 'rentals/new.html'
    fields = ('customer',)

    def get_success_url(self):
        book_id = self.kwargs.get('book_id')
        return reverse('rentals:detail', kwargs={'book_id':book_id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_id"] = self.kwargs.get('book_id')
        return context
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        book_id = self.kwargs.get('book_id')
        obj = Book.objects.get(id=book_id)
        instance.book = obj
        instance.status = '#0'
        instance.rent_start_date = datetime.now().date() 
        instance.save()
        return super().form_valid(form)
    

class SelectDownloadRentalsView(FormView):
    template_name = 'rentals/select_format.html'
    form_class = SelectExportOptionForm

    def get_success_url(self):
        return self.request.path
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = self.kwargs.get('book_id')
        context['book_id'] = book_id
        return context
    
    def post(self, request, **kwargs):
        formats = dict(FORMAT_CHOICES)
        format = self.request.POST.get('format')
        format = formats[format]

        book_id = self.kwargs.get('book_id')
        qs = Rental.objects.filter(Q(book__isbn=book_id) | Q(book__id=book_id))
        dataset = RentalResource().export(qs)

        if format == 'csv':
            ds = dataset.csv
        elif format == 'xls':
            ds = dataset.xls
        else:
            ds = dataset.json
        response = HttpResponse(ds, content_type=format)
        response['Content-Disposition'] = f'attachment; filename=rentals.{format}'
        return response