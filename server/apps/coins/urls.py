""""Рутер для приложения coins."""

from rest_framework.routers import SimpleRouter
from apps.coins.views import RateListView
from django.urls import path


router = SimpleRouter()

urlpatterns = [
    path('rates', RateListView.as_view())
]

urlpatterns += router.urls
