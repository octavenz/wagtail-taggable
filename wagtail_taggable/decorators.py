from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserViewSet

from wagtail import hooks

from wagtail_taggable.admin import TagChooser

_registry = {}


def register_tag(label: str, *, viewset_kwargs: dict = None):
    """Convenience wrapper that generates an admin chooser viewset and admin chooser widget for a tag model."""

    if viewset_kwargs is None:
        viewset_kwargs = {}

    def decorator(klass):

        url_base = f'{label.lower()}_chooser'

        class _Chooser(TagChooser):

            model = klass
            choose_modal_url_name = f'{url_base}:choose'

        _registry[klass.__name__] = {
            'class': klass,
            'chooser': _Chooser,
        }

        class _ChooserViewSet(ModelChooserViewSet):

            model = klass
            icon = viewset_kwargs.get('icon', 'tasks')
            page_title = _(f'Choose a {label}')
            per_page = viewset_kwargs.get('per_page', 10)

        @hooks.register('register_admin_viewset')
        def _register_viewset():
            return _ChooserViewSet(url_base, url_prefix=slugify(url_base))

        return klass
    return decorator
