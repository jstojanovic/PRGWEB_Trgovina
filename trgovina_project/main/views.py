from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from main.models import Proizvod, Kupac, Kosarica

class ProizvodListView(ListView):
    model = Proizvod
class KupacListView(ListView):
    model = Kupac

class KupacDetailView(DetailView):
    model = Kupac
    context_object_name = 'kupac'
    template_name = 'appname/kupac_detail.html'

class KupacCreateView(CreateView):
    model = Kupac
    fields = ['ime', 'prezime']
    template_name = 'appname/kupac_form.html'

class KupacUpdateView(UpdateView):
    model = Kupac
    fields = ['ime', 'prezime']
    template_name = 'appname/kupac_form.html'

class KupacDeleteView(DeleteView):
    model = Kupac
    success_url = '/kupci/'
    template_name = 'appname/kupac_confirm_delete.html'

class KosaricaListView(ListView):
    model = Kosarica
    context_object_name = 'kosarice'
    template_name = 'appname/kosarica_list.html'

class KosaricaDetailView(DetailView):
    model = Kosarica
    context_object_name = 'kosarica'
    template_name = 'appname/kosarica_detail.html'

class KosaricaCreateView(CreateView):
    model = Kosarica
    fields = ['kupac', 'proizvodi']
    template_name = 'appname/kosarica_form.html'

class KosaricaUpdateView(UpdateView):
    model = Kosarica
    fields = ['kupac', 'proizvodi']
    template_name = 'appname/kosarica_update.html'

class KosaricaDeleteView(DeleteView):
    model = Kosarica
    success_url = '/kosarice/'
    template_name = 'appname/kosarica_delete.html'

