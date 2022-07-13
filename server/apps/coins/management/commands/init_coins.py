from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help: str = "Инициализация валют."

    def handle(self, *args, **kwargs):
        self.stdout.write("Инициализация валют.")