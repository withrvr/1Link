from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from django.contrib import messages
from django.core.validators import MinValueValidator


# Custom User Model
class UsersProfile_Model(AbstractUser):

    def __init__(self, *args, **kwargs):
        super(UsersProfile_Model, self).__init__(*args, **kwargs)

        # override username validation
        self._meta.get_field('username').validators = [RegexValidator(
            r'^[0-9a-z_]+$',
            message="Enter a valid username. Only Numbers, Lowecase-Letter and UserScore ( _ ) is allowed"
        )]

    # OR: AbstractUser._meta.get_field('email').blank = False
    AbstractUser.email.field.blank = False
    AbstractUser.username.field.help_text = "Only Numbers, Lowecase-Letter and UserScore ( _ ) is allowed in Username"

    # Extended ( Extra ) ... fields of User
    display_Name = models.CharField(max_length=30, blank=True, null=True)
    profile_Picture = models.URLField(
        max_length=400, blank=True, null=True,
        default='https://raw.githubusercontent.com/withrvr/1Link/main/Images/Default_Profile_Picture.png',
    )
    banner_Image = models.URLField(
        max_length=400, blank=True, null=True,
        default='https://raw.githubusercontent.com/withrvr/1Link/main/Images/Default_Banner_Image.png',
    )
    clicks = models.IntegerField(
        default=0, blank=False, null=False,
        validators=[MinValueValidator(0), ]
    )

    """
    clicks
    unique_visitors

    bio
    location
    dob
    link
    category

    business email

    last_active
    show_last_active
    """

    def __str__(self, *args, **kwargs):
        return f'`{self.username}`'

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = "UsersProfile_Model"
        verbose_name_plural = "UsersProfile_Model"
