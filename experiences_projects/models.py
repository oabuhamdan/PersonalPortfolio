# Create your models here.
import wagtail.models
from wagtail.admin.panels import InlinePanel
from wagtail.models import Page, Orderable

from .experiences_model import *
from .projects_model import *


class ExperiencesPage(Page):
    parent_page_types = ['home.HomePage', ]
    max_count = 1
    date_format = models.CharField(max_length=15, default="M, Y")
    content_panels = Page.content_panels + [
        FieldPanel('date_format'),
        InlinePanel("work", heading="Work Experiences", min_num=0, classname="collapsed"),
    ]


class ProjectsPage(Page):
    parent_page_types = ['home.HomePage', ]
    max_count = 1
    content_panels = Page.content_panels + [
        InlinePanel("projects", heading="Projects", classname="collapsed"),
    ]
