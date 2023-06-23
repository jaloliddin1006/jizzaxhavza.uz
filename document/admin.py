from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import Article, ArticleCategory, ArticleImage

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    
class ArticleAdmin(admin.ModelAdmin):

    inlines = [ArticleImageInline]

    list_display = ['title', 'category', 'date']
    list_filter = ["category"]
    list_per_page =30
 
 
    

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)