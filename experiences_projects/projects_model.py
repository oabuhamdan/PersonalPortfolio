from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable

from home.wagtail_hooks import ProjectType


class Project(models.Model):
    project_title = models.CharField(max_length=255, default="")
    project_type = models.ForeignKey(ProjectType, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField("Year", default=2020)
    brief = models.CharField(help_text="250 characters at max", default="", max_length=250)
    tags = models.CharField(help_text="Split by ;", max_length=255, default="", blank=True)
    demo = models.URLField(max_length=255, default="", blank=True)
    code = models.URLField(max_length=255, default="", blank=True)
    video = models.URLField(max_length=255, default="", blank=True)
    slides = models.FileField(upload_to='documents', blank=True)
    description = RichTextField(default="", blank=True)

    panel = [
        FieldPanel('project_title'),
        FieldPanel('project_type'),
        FieldPanel('year'),
        FieldPanel('brief'),
        FieldPanel('tags'),
        FieldPanel('demo'),
        FieldPanel('code'),
        FieldPanel('video'),
        FieldPanel('slides'),
        FieldPanel('description'),
    ]


class ProjectsField(Project, Orderable):
    page = ParentalKey('ProjectsPage', related_name="projects", default=None)
