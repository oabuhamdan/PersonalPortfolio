from wagtail.admin.panels import *
from wagtail.models import Page

from .contact_page import *
from .home_page import *
from .item_list import *


class HomePage(Page):
    parent_page_types = ['wagtailcore.Page', ]
    name = models.CharField(max_length=50, default="")
    affiliation = models.CharField(max_length=150, default="")
    about = RichTextField(blank=True)
    max_count = 1

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('affiliation'),
            FieldPanel('about'),
            FieldPanel('image'),
        ], "Profile", classname="collapsed"),
        MultiFieldPanel([
            HelpPanel(
                "Icons supported now are (WhatsApp, Twitter, Facebook, Google Scholar, Linkedin, Github, and Email)"),
            InlinePanel('socialmedia', classname="collapsed", min_num=0, max_num=7),
        ], heading="Social Media Links", classname="collapsed"),
        InlinePanel("interests", heading="Interests", min_num=0, max_num=5, classname="collapsed"),
        InlinePanel("education", heading="Education", min_num=0, max_num=5, classname="collapsed"),
    ]


class ItemListPage(Page):
    parent_page_types = ['HomePage', ]
    date_format = models.CharField(max_length=15, default="M, Y")
    content_panels = Page.content_panels + [
        FieldPanel("date_format"),
        InlinePanel(relation_name="item_list", heading="Item List", min_num=0, classname="collapsed"),
    ]


class ContactPage(Page):
    parent_page_types = ['HomePage', ]
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=128, blank=True)
    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('location'),
        InlinePanel('extra_contact', heading="Extra Contact", classname="collapsed"),
    ]


class CustomHtmlPage(Page):
    parent_page_types = ['HomePage', ]
    html_main_code = models.TextField(default="", blank=True)
    html_side_code = models.TextField(default="", blank=True)
    css_code = models.TextField(default="", blank=True)
    js_code = models.TextField(default="", blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('html_main_code'),
        FieldPanel('html_side_code'),
        FieldPanel('css_code'),
        FieldPanel('js_code'),
    ]
