from django.db import models
from django.contrib.auth.models import AbstractUser


# creating custom user model
class UsersProfile_Model(AbstractUser):

    display_Name = models.CharField(max_length=30)
    profile_Picture = models.URLField(max_length=400, blank=True, null=True)
    banner_Image = models.URLField(max_length=400, blank=True, null=True)

    # making email field blank = False .... (ie. required)
    # OR: User._meta.get_field('email').blank = False
    AbstractUser.email.field.blank = False

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
