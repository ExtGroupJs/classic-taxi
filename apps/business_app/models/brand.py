from django.db import models


class Brand(models.Model):
    name = models.CharField(verbose_name="Name", unique=True, max_length=25)
    logo = models.ImageField(verbose_name="logo", null=True, blank=True)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return f"{self.name}"
