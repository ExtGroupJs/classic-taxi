from rest_framework import filters

from apps.business_app.models.car import Car
from apps.business_app.serializers.car import CarSerializer
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import AllowAny

from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet

from apps.common.mixins.common_view_mixin import CommonOrderingFilter


class CarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Car.objects.select_related("model")
    serializer_class = CarSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]
    filterset_fields = {
        "model": ["exact"],
        "model__brand": ["exact"],
        "air_conditioner": ["exact"],
        "enabled": ["exact"],
        "year": ["gte", "lte", "exact"],
        "mileage": ["gte", "lte", "exact"],
        "seats": ["gte", "exact"],
        "luggage": ["gte", "exact"],
    }

    search_fields = [
        "name",
        "model__name",
        "model__brand__name",
        "extra_info",
    ]
    ordering = ["name"]
    ordering_fields = [
        "name",
        "model__name",
        "model__brand__name",
    ]
