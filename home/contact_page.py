from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldRowPanel, FieldPanel


class ExtraContact(models.Model):
    icon = models.CharField("Name", max_length=50, default="")
    value = models.URLField("Link")
    panels = [
        FieldRowPanel([FieldPanel('icon'), FieldPanel('value')])
    ]


class ExtraContactField(ExtraContact):
    page = ParentalKey('ContactPage', related_name="extra_contact")
