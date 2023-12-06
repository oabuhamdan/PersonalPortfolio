import datetime

from django import template
from wagtail.images.models import Image

from home.wagtail_hooks import SupportedIcon
from mysite.settings.base import SHOW_WATERMARK

register = template.Library()


@register.simple_tag()
def site_icon():
    return Image.objects.filter(title="icon").first()


@register.simple_tag()
def site_logo():
    return Image.objects.filter(title="logo").first()


@register.simple_tag()
def social_media_icons(key):
    icon = SupportedIcon.objects.filter(name=key).first()
    return icon.html_class if icon else ""


@register.simple_tag()
def get_today():
    return datetime.date.today()


@register.simple_tag()
def show_watermark():
    return SHOW_WATERMARK


@register.filter
def get_semi_colon_sep_list(string):
    if isinstance(string, str):
        if len(string.strip()) > 0:
            return [s.strip() for s in string.split(";")]
        else:
            return []
    else:
        return string
