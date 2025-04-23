import django_filters

from apps.business_app.filters.lang_filter_mixin import LangFilterMixin
from apps.business_app.models.car import Car
from apps.business_app.models.driver import Driver


class DriverFilter(LangFilterMixin):
    class Meta:
        model = Driver
        fields = [
            "licence_year",
            "enabled",
            "car",
            "car__model",
            "car__model__brand",
        ]
