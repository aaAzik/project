from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='products/%Y/%m/%d/',null=True, blank=True )
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
