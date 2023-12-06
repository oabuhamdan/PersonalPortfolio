from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', on_delete=models.CASCADE, related_name='tagged_items')


class BlogIndexPage(Page):
    parent_page_types = ['home.HomePage', ]
    max_count = 1
    date_format = models.CharField(max_length=15, default="MM dd, Y")
    content_panels = Page.content_panels + [FieldPanel('date_format'), ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        blog_entries = BlogPage.objects.child_of(self).live()
        tag = request.GET.get('tag')
        if tag:
            blog_entries = blog_entries.filter(tags__name=tag)
        context['blog_entries'] = blog_entries
        return context


class BlogPage(Page):
    parent_page_types = [BlogIndexPage, ]
    short_description = models.CharField(max_length=100, default="")
    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.CASCADE,
        related_name='+'
    )
    date = models.DateField("Post date")
    body = RichTextField("Body", default="")
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('short_description'),
        FieldPanel('cover_image'),
        FieldPanel('date'),
        FieldPanel('tags'),
        FieldPanel('body'),
    ]
