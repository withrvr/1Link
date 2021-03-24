from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import UsersProfile_Model


# if profile_Picture, banner_Image
# of user is blank then setting it to the default images
@receiver(pre_save, sender=UsersProfile_Model)
def pre_images_url_to_default_if_blank(sender, instance, *args, **kwargs):

    if instance.profile_Picture is None:
        instance.profile_Picture = 'https://raw.githubusercontent.com/withrvr/1Link/main/Images/default_profile_picture.png'

    if instance.banner_Image is None:
        instance.banner_Image = 'https://raw.githubusercontent.com/withrvr/1Link/main/Images/default_banner_image.png'
