from rest_framework import filters

from apps.business_app.filters.driver import DriverFilter
from apps.business_app.models.driver import Driver
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import AllowAny

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.business_app.serializers.driver import DriverSerializer
from apps.common.mixins.common_view_mixin import CommonOrderingFilter
from django.db.models import F


class DriverViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]
    filterset_class = DriverFilter
    search_fields = [
        "name",
        "car__name",
        "car__model__name",
        "car__model__brand__name",
        "extra_info",
    ]
    ordering = ["name"]
    ordering_fields = [
        "name",
    ]

    def get_queryset(self):
        return self.queryset.annotate(
            extra_info=F(
                "extra_info_es"
            ),  # por defecto en español si no se especifica nada
        )
