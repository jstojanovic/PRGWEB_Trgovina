from django.urls import path
from main.views import ProizvodListView, KupacListView, KosaricaListView

urlpatterns = [
    path('proizvodi/', ProizvodListView.as_view()),
    path('kupci/', KupacListView.as_view()),
    path('kosarice/', KosaricaListView.as_view()),

]
