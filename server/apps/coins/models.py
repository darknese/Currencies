from django.db import models


class Rate(models.Model):
    """Модель для справочника валют."""

    name = models.CharField(max_length=255, help_text='Название')
    nominal = models.PositiveIntegerField(default=1, help_text='Номинал')
    code = models.CharField(max_length=8)


class Value(models.Model):
    """Модель с кешированными значениями валют"""
    num_code = models.PositiveIntegerField()
    char_code = models.CharField(max_length=5)
    date = models.DateField()
    value = models.DecimalField(max_digits=6, decimal_places=4)

    rate = models.ForeignKey(Rate, on_delete=models.CASCADE, null=False)
