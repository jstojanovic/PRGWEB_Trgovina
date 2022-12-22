import factory
from . import models

class KupacFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Kupac

    ime = factory.Faker('first_name')
    prezime = factory.Faker('last_name')

class ProizvodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Proizvod

    naziv = factory.Faker('word')
    cijena = factory.Faker('random_int', min=100, max=1000)

class KosaricaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Kosarica

    kupac = factory.SubFactory(KupacFactory)
    proizvodi = factory.RelatedFactory(ProizvodFactory, 'kosarica')

class NarudzbaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Narudzba

    kosarica = factory.SubFactory(KosaricaFactory)
    adresa_isporuke = factory.Faker('street_address')
    placena = factory.Faker('random_int', min=0, max=1)
