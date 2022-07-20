from datetime import datetime
from django.utils import timezone
from django_filters import rest_framework as filters
from django.http.request import QueryDict
from apps.coins.services import get_values


class ValueFilterBackend(filters.DjangoFilterBackend):
    """Класс фильтрации и обновления полей для запроса."""

    def get_filterset_kwargs(self, request, queryset, view):
        kwargs = super().get_filterset_kwargs(request, queryset, view)
        if hasattr(view, 'get_filterset_kwargs'):
            kwargs.update(view.get_filterset_kwargs())
        data: QueryDict = kwargs.get('data')
        date: datetime = datetime.strptime(data['date'], '%m/%d/%Y') \
            if 'date' in data \
            else timezone.now().date()
        # updated_data = QueryDict({
        #     'date': date.strftime('%m/%d/%Y')
        # })
        get_values(date.date())
        return kwargs
