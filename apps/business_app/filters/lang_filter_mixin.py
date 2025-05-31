import django_filters


class LangFilterMixin(django_filters.FilterSet):
    lang = django_filters.ChoiceFilter(
        method="lang_filter",
        choices=[("en", "English"), ("es", "Spanish"), ("fr", "French")],
    )

    def lang_filter(self, queryset, name, value):
        return queryset
