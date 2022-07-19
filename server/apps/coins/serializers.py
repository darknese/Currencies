"""Сериализация моделей для API."""

from rest_framework import serializers
from apps.coins.models import Rate, Value


class RateSerializer(serializers.ModelSerializer):
    """Класс сериализации валют."""

    class Meta:
        model = Rate
        fields = '__all__'


class ValueSerializer(serializers.ModelSerializer):
    """Класс сериализации валютных значений."""

    class Meta:
        model = Value
        fields = '__all__'
