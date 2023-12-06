from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet


class SupportedIcon(models.Model):
    name = models.CharField(max_length=25)
    html_class = models.CharField(max_length=100)


class IconsAdmin(SnippetViewSet):
    model = SupportedIcon
    menu_label = 'Supported Icon'
    icon = 'cog'
    add_to_settings_menu = False
    list_display = ('name', 'html_class')
    search_fields = ('name',)


class ProjectType(models.Model):
    type = models.CharField(max_length=120)

    def __str__(self):
        return self.type


class ProjectTypeAdmin(SnippetViewSet):
    model = ProjectType
    menu_label = 'Employment Type'
    icon = 'bars'
    add_to_settings_menu = False


class EmploymentType(models.Model):
    type = models.CharField(max_length=120)

    def __str__(self):
        return self.type


class EmploymentTypeAdmin(SnippetViewSet):
    model = EmploymentType
    menu_label = 'Project Type'
    icon = 'bars'
    add_to_settings_menu = False


# Now you just need to register your  ModelAdmin class with Wagtail
register_snippet(IconsAdmin)
register_snippet(ProjectTypeAdmin)
register_snippet(EmploymentTypeAdmin)
