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
        return 'nista'
