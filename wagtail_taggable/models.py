from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.search.index import Indexed


class BaseTag(Indexed, models.Model):
    """Provides base functionality for all tags."""

    name = models.CharField(
        unique=True,
        max_length=100,
    )

    slug = models.CharField(
        unique=True,
        max_length=100,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    search_fields = [
        index.SearchField('name'),
    ]

    panels = [
        FieldPanel('name'),
    ]
