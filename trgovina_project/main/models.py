from django.db import models

# Create your models here.
class Kupac(models.Model):
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)

    def __str__(self):
        return self.ime+' '+self.prezime

class Proizvod(models.Model):
    naziv = models.CharField(max_length=100)
    cijena = models.FloatField()

    def __str__(self):
        return self.naziv + ' ' + str(self.cijena)

class Kosarica(models.Model):
    proizvodi = models.ManyToManyField(Proizvod)
    kupac = models.ForeignKey(Kupac, on_delete=models.CASCADE)
    
    def __str__(self):
        proizvodi_str = ', '.join([str(proizvod) for proizvod in self.proizvodi.all()])
        return f'Kosarica for {self.kupac}: {proizvodi_str}'

class Narudzba(models.Model):
    kosarica = models.OneToOneField(Kosarica, on_delete=models.CASCADE)
    datum_narudzbe = models.DateTimeField(auto_now_add=True)
    adresa_isporuke = models.CharField(max_length=200)
    placena = models.BooleanField(default=False)
    def str(self):
        return f'Narudzba za {self.kosarica.kupac} u iznosu {self.iznos_narudzbe()} kn, placena: {self.placena}'
    def iznos_narudzbe(self):
        iznos = 0
        for proizvod in self.kosarica.proizvodi.all():
            iznos += proizvod.cijena
        return iznos

