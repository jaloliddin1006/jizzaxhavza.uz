from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import NavbarCategory, Contact


from mptt.admin import DraggableMPTTAdmin

class LetterAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"

admin.site.register(NavbarCategory, LetterAdmin)
