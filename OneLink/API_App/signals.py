from django.db.models.signals import post_save
from django.dispatch import receiver

from UsersProfile_App.models import UsersProfile_Model

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=UsersProfile_Model)
def create_Auth_Token(sender, instance, created, *args, **kwargs):

    if created:
        Token.objects.create(user=instance)
