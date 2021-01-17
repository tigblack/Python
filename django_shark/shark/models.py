from django.db import models
from datetime import date

from django.urls import reverse


class Human(models.Model):
    """Человек"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Люди"
        verbose_name_plural = "Люди"


class Shark(models.Model):
    """Акула"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    name = models.ManyToManyField(Human, verbose_name="человек", related_name="shark_human")
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shark_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Акула"
        verbose_name_plural = "Акулы"
