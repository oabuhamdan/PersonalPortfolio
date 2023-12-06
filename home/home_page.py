from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import *


class SocialMedia(models.Model):
    name = models.CharField("Name", max_length=50, default="")
    url = models.URLField("Link")
    panels = [
        FieldRowPanel([FieldPanel('name'), FieldPanel('url')])
    ]


class SocialMediaField(SocialMedia):
    page = ParentalKey('HomePage', related_name="socialmedia")


class Education(models.Model):
    title = models.CharField("Title", max_length=50, default="")
    university = models.CharField("University", max_length=100, default="")
    start_year = models.IntegerField("Starting Year", default=2020, null=True, blank=True)
    grad_year = models.IntegerField("Graduation Year", default=2020, null=True, blank=True)
    in_progress = models.BooleanField("In Progress?", default=False)
    location = models.CharField("Location", default="", max_length=100, blank=True)
    notes = models.CharField("notes", default="", max_length=150, blank=True,
                             help_text="GPA, Rank, Special Awards, etc.")
    panels = [
        FieldRowPanel([FieldPanel('title'), FieldPanel("university")]),
        FieldRowPanel([FieldPanel('start_year'), FieldPanel("grad_year"), FieldPanel("in_progress")]),
        FieldPanel('location'),
        FieldPanel('notes')
    ]


class EducationField(Education):
    page = ParentalKey('HomePage', related_name="education", default=None)


class Interests(models.Model):
    interest = models.CharField("Interest", max_length=100, default="")
    panels = [
        FieldPanel('interest'),
    ]


class InterestsField(Interests):
    page = ParentalKey('HomePage', related_name="interests")
