import django_filters

from apps.business_app.models.car import Car
from django.db.models import F


class LangFilterMixin(django_filters.FilterSet):
    lang = django_filters.ChoiceFilter(
        method="lang_filter",
        choices=[("en", "English"), ("es", "Spanish"), ("fr", "French")],
    )

    def lang_filter(self, queryset, name, value):
        return queryset.annotate(
            extra_info=F(f"extra_info_{value}"),
        )
