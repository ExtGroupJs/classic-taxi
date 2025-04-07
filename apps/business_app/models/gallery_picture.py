from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.business_app.models.car import Car


class GalleryPicture(models.Model):
    car = models.ForeignKey(
        to=Car,
        verbose_name="car",
        on_delete=models.CASCADE,
        related_name="car_gallery_pictures",
    )
    picture = models.ImageField(verbose_name=_("Main Picture"))

    extra_info = models.TextField(verbose_name="Extra Info", null=True, blank=True)

    class Meta:
        verbose_name = _("Gallery Picture")
        verbose_name_plural = _("Gallery Pictures")

    def __str__(self):
        return f"{self.car}"
