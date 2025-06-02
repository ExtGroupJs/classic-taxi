from rest_framework import filters

from apps.business_app.models.client import Client
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import AllowAny

from rest_framework.viewsets import GenericViewSet, ModelViewSet


from apps.business_app.serializers.client import ClientSerializer
from apps.common.mixins.common_view_mixin import CommonOrderingFilter


class ClientViewSet(ModelViewSet, GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]

    ordering = ["first_name"]
    ordering_fields = [
        "first_name",
        "last_name",
    ]
