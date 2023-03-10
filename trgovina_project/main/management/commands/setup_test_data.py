import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Kupac, Proizvod, Kosarica, Narudzba
from main.factories import (
    KupacFactory,
    ProizvodFactory,
    KosaricaFactory,
    NarudzbaFactory
)

NUM_KUPACS = 10
NUM_PROIZVODS = 15
NUM_KOSARICAS = 4
NUM_NARUDZBAS = 7
class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Kupac, Proizvod, Kosarica]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_KUPACS):
            kupac = KupacFactory()

        for _ in range(NUM_PROIZVODS):
            proizvod = ProizvodFactory()
        
        for _ in range(NUM_KOSARICAS):
            kosarica = KosaricaFactory()
        for _ in range(NUM_NARUDZBAS):
            kosarica = NarudzbaFactory()



