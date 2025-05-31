# models.py


from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel
from django.core.cache import cache


class GlobalSiteData(SingletonModel):
    visitors_counter = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = _("Global Site Data")
