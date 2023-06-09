from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Cart


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Cart.objects.create(user=instance)


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_profile(sender, instance, **kwargs):
#     instance.my_cart.save()
