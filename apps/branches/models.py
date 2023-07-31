from django.db import models
from apps.base.models import Base


# Create your models here.


class Branch(Base):
    name = models.CharField("Name", max_length=30, null=False, blank=False)
    country = models.CharField("Country", max_length=30, null=False, blank=False)
    state = models.CharField("State", max_length=30, null=False, blank=False)
    city = models.CharField("City", max_length=30, null=False, blank=False)

    def natural_key(self):
        return self.name

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"


class Area(Base):
    name = models.CharField("Name", max_length=30, null=False, blank=False)
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE, null=False, blank=False
    )

    def natural_key(self):
        return self.name

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"


class Subarea(Base):
    name = models.CharField("Name", max_length=30, null=False, blank=False)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=False, blank=False)

    def natural_key(self):
        return self.name

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Subarea"
        verbose_name_plural = "Subareas"
