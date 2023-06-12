from django.db import models

# Create your models here.

from django.db import models
from mptt.models import MPTTModel

from mptt.fields import TreeForeignKey

class NavbarCategory(MPTTModel):
    STATUS = (
        ('navbar', 'Navbar'),
        ('sidebar', 'Sidebar'),
        
    )
    status = models.CharField(choices=STATUS, max_length=100, default='navbar')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icon/', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
