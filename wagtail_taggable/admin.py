from generic_chooser.widgets import AdminChooser

from wagtail.admin.panels import InlinePanel


class TagsPanel(InlinePanel):
    """Custom Inline Panel variant with simplified UI for rendering lists of tags."""

    def classes(self):
        # InlinePanel renders with the nested panel interface, but we don't need that here.
        return [class_ for class_ in super().classes() if class_ != 'w-panel--nested']

    class BoundPanel(InlinePanel.BoundPanel):
        template_name = 'wagtail_taggable/tags_panel.html'

        class Media:
            css = {
                'all': ('wagtail_taggable/css/tag-panel.css',),
            }


class TagChooser(AdminChooser):
    template = 'wagtail_taggable/tag_chooser.html'
