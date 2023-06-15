from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import NavbarCategory, Contact


from mptt.admin import DraggableMPTTAdmin

class LetterAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"

class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "date", "phone"]
    
admin.site.register(Contact, ContactAdmin)
admin.site.register(NavbarCategory, LetterAdmin)
