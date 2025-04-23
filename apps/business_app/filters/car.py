import django_filters

from apps.business_app.filters.lang_filter_mixin import LangFilterMixin
from apps.business_app.models.car import Car


class CarFilter(LangFilterMixin):
    class Meta:
        model = Car
        fields = {
            "model": ["exact"],
            "model__brand": ["exact"],
            "air_conditioner": ["exact"],
            "enabled": ["exact"],
            "year": ["gte", "lte", "exact"],
            "mileage": ["gte", "lte", "exact"],
            "seats": ["gte", "exact"],
            "luggage": ["gte", "exact"],
        }
