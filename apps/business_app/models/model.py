from django.db import models

from apps.business_app.models.brand import Brand


class Model(models.Model):
    name = models.CharField(verbose_name="Name", unique=True, max_length=250)
    brand = models.ForeignKey(to=Brand, verbose_name="Brand", on_delete=models.CASCADE)
    extra_info = models.TextField(verbose_name="Extra Info", null=True, blank=True)

    class Meta:
        verbose_name = "Model"
        verbose_name_plural = "Models"

    def __str__(self):
        return f"{self.name} ({self.brand})"
