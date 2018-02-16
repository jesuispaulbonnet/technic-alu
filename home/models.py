from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.functional import cached_property
from django.conf import settings

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import (
    InlinePanel,
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtailgeowidget.legacy_edit_handlers import GeoPanel
from wagtailgeowidget.helpers import geosgeometry_str_to_struct


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

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class ContactPage(Page):
    def get_context(self, request):
        context = super(ContactPage, self).get_context(request)
        context.update(get_base_context())
        context.update({
            'api_key': settings.GOOGLE_MAPS_V3_APIKEY
        })
        return context

    address = models.CharField(max_length=250, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('address'),
            GeoPanel('location', address_field='address'),
        ], ('Geo details')),
    ]

    @cached_property
    def point(self):
        return geosgeometry_str_to_struct(self.location)

    @property
    def lat(self):
        return self.point['y']

    @property
    def lng(self):
        return self.point['x']
