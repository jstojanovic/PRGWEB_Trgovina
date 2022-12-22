# in factories.py
import factory

class KupacFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'main.Kupac'
    
    ime = factory.Faker('first_name')
    prezime = factory.Faker('last_name')

class ProizvodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'main.Proizvod'

    naziv = factory.Faker('word')
    cijena = factory.Faker('pyfloat')

class KosaricaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'main.Kosarica'

    kupac = factory.SubFactory(KupacFactory)
    proizvodi = factory.RelatedFactory(ProizvodFactory, 'kosarica')

