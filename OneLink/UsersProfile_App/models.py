from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# creating custom user model


class UsersProfile_Model(AbstractUser):

    # making email field blank = False .... (ie. required)
    # OR: User._meta.get_field('email').blank = False
    AbstractUser.email.field.blank = False

    # Extended ( Extra ) ... fields of User
    display_Name = models.CharField(max_length=30, blank=True, null=True)
    profile_Picture = models.URLField(
        max_length=400, blank=True, null=True,
        default='https://raw.githubusercontent.com/withrvr/1Link/main/Images/default_profile_picture.png',
    )
    banner_Image = models.URLField(
        max_length=400, blank=True, null=True,
        default='https://raw.githubusercontent.com/withrvr/1Link/main/Images/default_banner_image.png',
    )

    """
    bio
    location
    dob
    link
    category

    last_active
    show_last_active
    """

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = _("UsersProfile_Model")
        verbose_name_plural = _("UsersProfile_Model")
