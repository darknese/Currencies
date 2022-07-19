from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters
from apps.coins.models import Rate, Value
from apps.coins.serializers import RateSerializer, ValueSerializer
from apps.coins.backends import ValueFilterBackend


class RateListView(ListAPIView):

    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = (AllowAny,)


class ValueListView(ListAPIView):
    serializer_class = ValueSerializer
    filter_backends = (ValueFilterBackend,)
    filterset_fields = ('date', 'rate__code',)
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Value.objects.all()
