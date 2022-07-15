from django.core.management.base import BaseCommand
from apps.coins.models import Rate
from apps.coins.services import get_rates


class Command(BaseCommand):
    help: str = "Инициализация валют."

    def handle(self, *args, **kwargs):
        rates = get_rates()
        Rate.objects.bulk_create([
            Rate(**rate) for rate in rates
        ])
        self.stdout.write("Инициализация валют.")