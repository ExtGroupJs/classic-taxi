from rest_framework import filters

from apps.business_app.models.gallery_picture import GalleryPicture
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import AllowAny

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.business_app.serializers.gallery_picture import GalleryPictureSerializer
from apps.common.mixins.common_view_mixin import CommonOrderingFilter


class GalleryPictureViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = GalleryPicture.objects.all()
    serializer_class = GalleryPictureSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]
    filterset_fields = [
        "car",
    ]

    ordering = ["car"]
