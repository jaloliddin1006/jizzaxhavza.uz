from django.db import models
from mptt.models import MPTTModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from mptt.fields import TreeForeignKey
from document.models import ArticleCategory
class NavbarCategory(MPTTModel):
    STATUS = (
        ('navbar', 'Navbar'),
        ('sidebar', 'Sidebar'),
        
    )
    ordered = models.IntegerField( null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=100, default='navbar')
    article = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icon/', null=True, blank=True)
    icon_thumbnail = ImageSpecField(source='icon',
                                    processors=[ResizeToFit(100, 100)],
                                    format='JPEG',
                                    options={'quality': 80})
    class MPTTMeta:
        order_insertion_by = ['ordered']

    def __str__(self):
        return self.name

    def has_children(self):
        return self.get_children().exists()
    
    
    def is_root(self):
        return self.is_root_node()
    
    
    
    
class Contact(models.Model):
    name = models.CharField(max_length=150, verbose_name="Ismingizni kiriting: ")
    phone = models.CharField(max_length=150, verbose_name="Telefon raqamingiz:")
    body = models.TextField(verbose_name="O'zingizni qiziqtirgan savol yoki takliflaringizni yozishingiz mumkin:")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)