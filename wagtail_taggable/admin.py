from generic_chooser.widgets import AdminChooser

from wagtail.admin.panels import InlinePanel


class TagsPanel(InlinePanel):
    """Custom Inline Panel variant with simplified UI for rendering lists of tags."""

    class BoundPanel(InlinePanel.BoundPanel):
        template_name = 'tags/tags_panel.html'

        class Media:
            css = {
                'all': ('tags/css/tag-panel.css',)
            }


class TagChooser(AdminChooser):
    template = 'tags/tag_chooser.html'
