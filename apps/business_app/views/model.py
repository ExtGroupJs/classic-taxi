from rest_framework import filters

from apps.business_app.models.model import Model
from apps.business_app.serializers.model import ModelSerializer
from django_filters.rest_framework import DjangoFilterBackend

from django.db.models import F
from rest_framework.permissions import AllowAny

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.common.mixins.common_view_mixin import CommonOrderingFilter


class ModelViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Model.objects.all().annotate(brand_name=F("brand__name"))
    serializer_class = ModelSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]
    filterset_fields = [
        "brand",
    ]
    search_fields = [
        "name",
        "extra_info",
    ]
    ordering = ["name"]
    ordering_fields = [
        "name",
        "brand_name",
    ]
