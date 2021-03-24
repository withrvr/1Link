from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsersProfile_Model
from django.core.exceptions import ValidationError


# creating new user form
class UsersProfile_CreationForm(UserCreationForm):

    cant_use_this_username = [
        'admin',

        'login',
        'logout',
        'register',

        'about',
        'home',
    ]

    def __init__(self, *args, **kwargs):
        super(UsersProfile_CreationForm, self).__init__(*args, **kwargs)

        self.fields[
            'username'].help_text = "Only Numbers, Lowecase-Letter and UserScore ( _ ) is allowed in Username"

    def clean_username(self, *args, **kwargs):
        import re
        validate_username = self.cleaned_data['username']

        if not re.match(r'^[0-9a-z_]+$', validate_username):
            raise ValidationError(
                f"Only Numbers, Lowecase-Letter and UserScore ( _ ) is allowed in Username")

        elif validate_username in self.cant_use_this_username:
            raise ValidationError(
                f" Username `{validate_username}` can't be use ... try some other username")

        return validate_username

    class Meta(UserCreationForm.Meta):
        model = UsersProfile_Model
        fields = UserCreationForm.Meta.fields + (
            'username', 'email',
        )
