from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldRowPanel, FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable

from home.wagtail_hooks import EmploymentType


class Experience(models.Model):
    title = models.CharField("Title", max_length=50, default="")
    employment_type = models.ForeignKey(EmploymentType, on_delete=models.SET_NULL, null=True)
    company_name = models.CharField("Company Name", default="", max_length=255)
    location = models.CharField("Location", default="", max_length=50, blank=True)
    start_date = models.DateField()
    still_working_here = models.BooleanField(default=False)
    end_date = models.DateField(blank=True, default=None, null=True)
    main_skills = models.CharField(help_text="Split by ;", max_length=255, default="", blank=True, null=True)
    description = RichTextField("Description", default="", blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('employment_type'),
        FieldPanel('company_name'),
        FieldPanel('location'),
        FieldRowPanel([FieldPanel('start_date'), FieldPanel("end_date"), FieldPanel('still_working_here')]),
        FieldPanel('main_skills'),
        FieldPanel('description')
    ]


class ExperienceField(Experience, Orderable):
    page = ParentalKey('ExperiencesPage', related_name="work", default=None)
