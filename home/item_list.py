from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import *
from django.utils import timezone
from wagtail.fields import RichTextField


class ItemList(models.Model):
    date = models.DateField(default=timezone.now)
    text = RichTextField(default="", max_length=500)
    panels = [
        FieldPanel('date'),
        FieldPanel('text')
    ]

    class Meta:
        ordering = ("-date",)


class ItemListField(ItemList):
    page = ParentalKey('ItemListPage', related_name="item_list")
