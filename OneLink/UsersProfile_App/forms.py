from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import UsersProfile_Model


# currently in clean username method
# checking if this username is allowed to be used
def comman_clean_username_method(self, *args, **kwargs):

    # cant use this username
    # as your username
    cant_use_this_username = [
        'admin-page'
        'login',
        'logout',
        'register',

        'home',
        'about',
    ]

    validate_username = self.cleaned_data["username"]

    if validate_username in cant_use_this_username:
        raise forms.ValidationError(
            f"Enter a valid username ... Can't use ''{validate_username}'' as username ... Try Something New"
        )

    return validate_username


# creating new user form
class UsersProfile_CreationForm(UserCreationForm):

    def clean_username(self, *args, **kwargs):
        return comman_clean_username_method(self, *args, **kwargs)

    class Meta(UserCreationForm.Meta):
        model = UsersProfile_Model
        fields = UserCreationForm.Meta.fields + (
            'username', 'email',
        )


# Update users information
class UsersProfile_ChangeForm(UserChangeForm):

    def clean_username(self, *args, **kwargs):
        return comman_clean_username_method(self, *args, **kwargs)

    class Meta(UserChangeForm.Meta):
        model = UsersProfile_Model
        fields = (
            'username',
            'email',
            'display_Name',
            'profile_Picture',
            'banner_Image',
        )
