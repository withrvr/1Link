from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import UsersProfile_Model


# checking if this username is allowed to be used or not
def is_username_allowed(self, *args, **kwargs):
    validate_username = self.cleaned_data["username"]

    import cant_use_this_name
    if validate_username in cant_use_this_name.cant_use_this_name:
        raise forms.ValidationError(
            f"Can't use ''{validate_username}'' as username - Try Something else"
        )
    return validate_username


# creating new user form
class UsersProfile_CreationForm(UserCreationForm):

    def clean_username(self, *args, **kwargs):
        return is_username_allowed(self, *args, **kwargs)

    class Meta(UserCreationForm.Meta):
        model = UsersProfile_Model
        fields = UserCreationForm.Meta.fields + (
            'username', 'email',
        )


# Update users information
class UsersProfile_ChangeForm(UserChangeForm):

    def clean_username(self, *args, **kwargs):
        return is_username_allowed(self, *args, **kwargs)

    class Meta(UserChangeForm.Meta):
        model = UsersProfile_Model
        fields = (
            'username',
            'email',
            'display_Name',
            'profile_Picture',
            'banner_Image',
        )
