from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse(b'pogledi su na: <strong>localhost:8000/{proizvodi, narudzbe, kosarice, kupci}</strong>')
    # primjetiti korištenje HTML-a
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from main.models import Proizvod, Kupac, Kosarica, Narudzba

class ProizvodListView(ListView):
    model = Proizvod
class KupacListView(ListView):
    model = Kupac

class KosaricaListView(ListView):
    model = Kosarica

class NarudzbaListView(ListView):
    model = Narudzba
