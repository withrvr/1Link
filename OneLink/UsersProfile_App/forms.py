from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UsersProfile_Model


# creating new user form
class UsersProfile_CreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UsersProfile_Model
        fields = UserCreationForm.Meta.fields + (
            'username', 'email',
        )


# Update users information
class UsersProfile_ChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = UsersProfile_Model
        fields = (
            'username',
            'email',
            'display_Name',
            'profile_Picture',
            'banner_Image',
        )

    # def clean_username(self, *args, **kwargs):
    #     import re
    #     validate_username = self.cleaned_data['username']

    #     if not re.match(r'^[0-9a-z_]+$', validate_username):
    #         raise ValidationError(
    #             f"Only Numbers, Lowecase-Letter and UserScore ( _ ) is allowed in Username")

    #     elif validate_username in cant_use_this_username:
    #         raise ValidationError(
    #             f" Username `{validate_username}` can't be use ... try some other username")

    #     return validate_username
