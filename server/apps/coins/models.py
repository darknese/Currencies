from django.db import models


class Rate(models.Model):
    """"Модель для справочника валют."""

    name = models.CharField(max_length=255, help_text='Название')
    nominal = models.PositiveIntegerField(default=1,help_text='Номинал')
    code = models.CharField(max_length=8)