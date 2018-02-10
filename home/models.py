from __future__ import absolute_import, unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import (
    InlinePanel,
    FieldPanel,
)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.api import APIField
from wagtail.wagtailimages.api.fields import ImageRenditionField


def get_base_context():
    context = {}
    context['gallery_pages'] = GalleryPage.objects.live().in_menu()
    return context


class HomePage(Page):
    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context.update(get_base_context())
        return context

    content_panels = Page.content_panels + [
        InlinePanel('carousel_images', label="Carousel Images"),
    ]


class CarouselImage(Orderable):
    page = ParentalKey(
        HomePage,
        on_delete=models.CASCADE,
        related_name='carousel_images'
    )

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('subtitle'),
    ]


class GalleryPage(Page):
    def get_context(self, request):
        context = super(GalleryPage, self).get_context(request)
        context.update(get_base_context())
        return context

    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        InlinePanel('gallery_images', label="Gallery Images"),
    ]

    api_fields = [
        APIField('gallery_images')
    ]


class GalleryImage(Orderable):
    page = ParentalKey(
        GalleryPage,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )

    caption = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='gallery_image'
    )

    api_fields = [
        APIField('caption'),
        APIField('image'),
        APIField('image_thumbnail', serializer=ImageRenditionField('fill-300x200', source='image'))
    ]

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
