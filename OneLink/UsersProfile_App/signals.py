from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UsersProfile_Model


# if profile_Picture, banner_Image
# of user is blank then setting it to the default images
@receiver(post_save, sender=UsersProfile_Model)
def images_url_to_default_if_blank(sender, instance, created, ** kwargs):
    # print()
    # print(instance.profile_Picture)
    # print(instance.banner_Image)
    # print(created)
    # print()

    if instance.profile_Picture in (None, ''):
        UsersProfile_Model.objects.filter(username=instance.username).update(
            profile_Picture='https://raw.githubusercontent.com/withrvr/1Link/main/Images/default_profile_picture.png'
        )

    if instance.banner_Image in (None, ''):
        UsersProfile_Model.objects.filter(username=instance.username).update(
            banner_Image='https://raw.githubusercontent.com/withrvr/1Link/main/Images/default_banner_image.png'
        )
