from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, HelpPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class PublicationsPage(Page):
    parent_page_types = ['home.HomePage', ]
    max_count = 1

    name_as_in_author = models.CharField(max_length=255, default="")

    content_panels = Page.content_panels + [
        FieldPanel('name_as_in_author'),
        InlinePanel("conferences", heading="Conference Papers", classname="collapsed"),
        InlinePanel("journals", heading="Journal Papers", classname="collapsed"),
        InlinePanel("book_chapters", heading="Book Chapters", classname="collapsed"),
        InlinePanel("books", heading="Books", classname="collapsed"),
    ]


class BasicPublication(models.Model):
    publication_title = models.CharField(max_length=255, default="")
    publication_date = models.DateField(blank=True, null=True)
    authors = models.CharField(max_length=255, default="", blank=True)
    doi = models.URLField(max_length=255, default="", blank=True)
    bib = models.TextField(default="", blank=True)
    custom_styled_info = RichTextField(default="", blank=True,
                                       help_text="Enter info here with your custom style. "
                                                 "Leave it empty and use below fields to use default style")

    panels = [
        FieldPanel('publication_title'),
        FieldPanel('custom_styled_info'),
        FieldPanel('publication_date'),
        FieldPanel('authors'),
        FieldPanel('doi'),
        FieldPanel('bib'),
    ]

    class Meta:
        ordering = ('-publication_date',)


class Papers(BasicPublication):
    published_in = models.CharField(max_length=255, default="", blank=True)
    pages = models.CharField(max_length=255, blank=True, default="")
    abstract = models.TextField(default="", blank=True)

    panels = BasicPublication.panels + [
        FieldPanel('published_in', help_text="Conference or Journal name"),
        FieldPanel('pages'),
        FieldPanel('abstract'),
    ]


class JournalPapers(Papers):
    volume = models.CharField(max_length=255, blank=True, default="")
    issue = models.CharField(max_length=255, blank=True, default="")
    panels = Papers.panels + [
        FieldPanel('volume'),
        FieldPanel('issue'),
    ]


class ConferencePapers(Papers):
    video = models.URLField(blank=True, default="", help_text="Use a valid URL")
    slides = models.FileField(upload_to="documents", blank=True)

    panels = Papers.panels + [
        FieldPanel('video'),
        FieldPanel('slides'),
    ]


class Book(BasicPublication):
    publisher = models.CharField(max_length=255, blank=True, default="")

    panels = BasicPublication.panels + [
        FieldPanel('publisher'),
    ]


class BookChapter(Book):
    book_details = models.CharField(max_length=500, default="", blank=True)
    pages = models.CharField(max_length=255, blank=True, default="")
    panels = Book.panels + [
        FieldPanel('book_details'),
        FieldPanel('pages'),
    ]


class ConferencePapersField(ConferencePapers):
    page = ParentalKey('PublicationsPage', related_name="conferences", default=None)


class JournalPapersField(JournalPapers):
    page = ParentalKey('PublicationsPage', related_name="journals", default=None)


class BooksField(Book):
    page = ParentalKey('PublicationsPage', related_name="books", default=None)


class BookChaptersField(BookChapter):
    page = ParentalKey('PublicationsPage', related_name="book_chapters", default=None)
