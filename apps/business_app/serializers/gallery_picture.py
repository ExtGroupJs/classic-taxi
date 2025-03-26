from rest_framework import serializers

from apps.business_app.models.gallery_picture import GalleryPicture


class GalleryPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryPicture
        fields = (
            "id",
            "car",
            "picture",
            "extra_info",
            "__str__",
        )
