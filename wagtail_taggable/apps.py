from django.apps import AppConfig
from django.db.models import ForeignKey


class WagtailTaggableConfig(AppConfig):
    name = 'wagtail_taggable'

    def ready(self):

        # Set up model forms to use TagChooser derivative for any ForeignKey to a tag model
        from wagtail.admin.forms.models import register_form_field_override
        from .decorators import _registry

        for class_name, values in _registry.items():
            register_form_field_override(
                ForeignKey, to=values['class'], override={"widget": values['chooser']}
            )
