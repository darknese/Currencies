from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from apps.coins.models import Rate
from apps.coins.serializers import RateSerializer



class RateListView(ListAPIView):

    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = (AllowAny,)