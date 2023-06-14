from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import Article, ArticleCategory, ArticleImage

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    
class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

    list_display = ['title', 'category', 'date']
    inlines = [ArticleImageInline]
    
    
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)