""""Сериализация моделей для API."""

from rest_framework import serializers
from apps.coins.models import Rate


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'
