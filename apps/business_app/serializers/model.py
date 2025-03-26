from rest_framework import serializers

from apps.business_app.models.model import Model


class ModelSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(read_only=True)

    class Meta:
        model = Model
        fields = (
            "id",
            "name",
            "brand",
            "brand_name",
            "extra_info",
            "__str__",
        )
