from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book, Contact, Passenger
from django.urls import reverse_lazy
from .forms import ContactForm

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.db.models import Count, Q


def chart(request):
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')
    return render(request, 'chart/chart.html', {'dataset': dataset})

class BookList(ListView):
    model = Book

class BookView(DetailView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = ['name','author', 'pages','image']
    success_url = reverse_lazy('book_list')

class BookUpdate(UpdateView):
    model = Book
    fields = ['name','author', 'pages','image']
    success_url = reverse_lazy('book_list')

class BookDelete(DeleteView):
    model = Book
    #messages.add_message(request, messages.INFO, 'Data Delete Successfully')
    success_url = reverse_lazy('book_list')

class ContactCreate(CreateView):
    model = Contact
    template_name="contact/contact_form.html"
    fields = ['first_name','last_name', 'email','message']
    success_url = reverse_lazy('home')

class PassengerCreate(CreateView):
    model = Passenger
    template_name="chart/passenger_form.html"
    fields = ['name', 'survived','ticket_class']
    success_url = reverse_lazy('chart')

class PassengerList(ListView):
    model = Passenger
class ContactList(ListView):
    model = Contact
#    template_name = "contact/contact_list.html"
