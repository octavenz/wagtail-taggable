from django.db import models

from django.utils.translation import gettext_lazy as _

from wagtail.search import index
from wagtail.search.index import Indexed


class BaseTag(Indexed, models.Model):
    """Provides base functionality for all tags."""

    name = models.CharField(
        unique=True,
        max_length=100,
        help_text=_('Note: tag names are always saved in lower case.')
    )

    def __str__(self):
        return self.name.title()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super().save(*args, **kwargs)

    search_fields = [
        index.SearchField('name'),
    ]


# TODO: deprecate? automate? - RichC
class TagField(models.ForeignKey):
    """Custom foreign key field that uses a custom tag chooser in the admin interface."""
    pass
