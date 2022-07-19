""""Рутер для приложения coins."""

from rest_framework.routers import SimpleRouter
from apps.coins.views import RateListView, ValueListView
from django.urls import path


router = SimpleRouter()

urlpatterns = [
    path('rates/', RateListView.as_view()),
    path('values/', ValueListView.as_view()),
]

urlpatterns += router.urls
