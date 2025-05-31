from ast import arg
from rest_framework import filters

from apps.business_app.filters.car import CarFilter
from apps.business_app.models.car import Car
from apps.business_app.serializers.car import CarSerializer
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import AllowAny

from rest_framework import viewsets
from django.db.models import F
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
    # filterset_fields = {
    #     "model": ["exact"],
    #     "model__brand": ["exact"],
    #     "air_conditioner": ["exact"],
    #     "enabled": ["exact"],
    #     "year": ["gte", "lte", "exact"],
    #     "mileage": ["gte", "lte", "exact"],
    #     "seats": ["gte", "exact"],
    #     "luggage": ["gte", "exact"],
    # }
    filterset_class = CarFilter
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

    def get_queryset(self):
        # por defecto en español si no se especifica nada
        return self.queryset.annotate(
            extra_info=F(f"extra_info_{self.request.LANGUAGE_CODE}"),
        )
