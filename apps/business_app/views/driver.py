from rest_framework import filters

from apps.business_app.models.driver import Driver
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import AllowAny

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.business_app.serializers.driver import DriverSerializer
from apps.common.mixins.common_view_mixin import CommonOrderingFilter


class DriverViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]
    filterset_fields = [
        "licence_year",
        "enabled",
        "car",
        "car__model",
        "car__model__brand",
    ]
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
