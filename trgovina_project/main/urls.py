from django.urls import path
from main.views import ProizvodListView, KupacListView, KosaricaListView, NarudzbaListView
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('proizvodi/', ProizvodListView.as_view()),
    path('kupci/', KupacListView.as_view()),
    path('kosarice/', KosaricaListView.as_view()),
    path('narudzbe/', NarudzbaListView.as_view()),

]
