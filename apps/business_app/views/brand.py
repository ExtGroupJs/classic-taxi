from rest_framework import filters
from apps.business_app.models.brand import Brand
from apps.business_app.serializers.brand import BrandSerializer
from django_filters.rest_framework import DjangoFilterBackend


from apps.common.mixins.common_view_mixin import CommonOrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class BrandViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]

    search_fields = [
        "name",
    ]
