from django.db import models
from ckeditor.fields import RichTextField


class ArticleCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
    
class Article(models.Model):
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=400, null=True, blank=True)
    description = RichTextField()
    views = models.IntegerField(default=0)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
    
class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article/', null=True, blank=True)
    
    def __str__(self):
        return str(self.article)
    