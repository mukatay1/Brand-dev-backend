from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Item(models.Model):
    title = models.CharField(
        max_length=255
    )
    description = models.TextField()
    price = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        default=0
    )
    count = models.IntegerField(default=0)
    image = CloudinaryField(
        'image',
        default=None,
        null=True
    )

    def __str__(self):
        return self.title
