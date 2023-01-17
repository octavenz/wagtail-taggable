# Wagtail Taggable

Simple tag functionality for Wagtail sites wanting curated tags without the complexity.

## Installation & Setup

Install with pip

    pip install wagtail-taggable

    or

    poetry add wagtail-taggable

## Add to Django installed apps

    INSTALLED_APPS = [
        #...
        'wagtail_taggable',
    ]

## Setup your tag models

Using the `register_tag` decorator automatically sets up any `ForeignKey` references to the decorated model to render using a chooser widget specifically for your tag model. It takes care of registering all the form widgets and urls needed to get this interface working.

    @register_tag('Example')
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

![Screenshot](https://github.com/octavenz/wagtail-taggable/blob/main/tags-interface.png)

## Query items based on tags

Perform queries based on tags like you would with any other related table

    tagged_items = (
        ExamplePage.objects
        .filter(example_tag_relationship__example_tag__name='My Cool Tag')
    )
