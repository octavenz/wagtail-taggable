# Wagtail Taggable

Simple tag functionality for Wagtail sites wanting curated tags without the complexity.

## Installation & Setup

Install with pip

    pip install wagtail-favicon
    
    or
    
    poetry add wagtail-favicon

## Add to Django installed apps

    INSTALLED_APPS = [
        #...
        'wagtail_taggable',
    ]

## Setup your tag models

    @register_tag('Example')  # <-- sets up the admin chooser and urls for using tags
    class ExampleTag(BaseTag):
    
        class Meta:
            verbose_name = _('Example')


## Optionally expose Tag models using Model Admin

    from django.apps import apps
    from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup

    class ExampleTagModelAdmin(ModelAdmin):
    
        @property
        def model(self):
            return apps.get_model('app.ExampleTag')
    
        menu_label = 'Example'
        menu_icon = 'tasks'
        menu_order = 100
        list_display = ('name',)
    
    
    class TagsModelAdminGroup(ModelAdminGroup):
    
        menu_label = 'Tags'
        menu_icon = 'tag'
        menu_order = 502
        items = [
            ExampleTagModelAdmin,
        ]

    from app.admin.tags import TagsModelAdminGroup

    modeladmin_register(TagsModelAdminGroup)


## Use tags on page models (or any other model)

1. Define through relationship:


    class ExamplePageExampleTagRelationship(models.Model):
    
        page = ParentalKey(
            'app.ExamplePage',
            on_delete=models.CASCADE,
            related_name='example_tag_relationships',
            related_query_name='example_tag_relationship',
        )
    
        example_tag = models.ForeignKey(
            'app.ExampleTag',
            on_delete=models.CASCADE,
            related_name='example_page_relationships',
            related_query_name='example_page_relationship',
        )

2. Use TagsPanel to render the tags interface in the CMS for the taggable model (in this case a wagtail.Page)


    class ExamplePage(Page):

        ...

        content_panels = [
            TagsPanel('example_tag_relationships', heading='Example Tags'),
        ]

## Query items based on their tags like you would with any other related table

    tagged_items = (
        ExamplePage.objects
        .filter(example_tag_relationship__example_tag__name='My Cool Tag')
    )
               