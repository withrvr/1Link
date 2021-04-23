from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from UsersProfile_App.models import UsersProfile_Model
from django.forms import ValidationError


# custom user login AuthenticationForm
class Users_Login_AuthenticationForm(AuthenticationForm):
    def clean_username(self, *args, **kwargs):
        form_username = self.cleaned_data["username"]
        try:
            UsersProfile_Model.objects.get(username=form_username)
        except UsersProfile_Model.DoesNotExist:
            raise ValidationError(
                f"There is no Account with Username ''{form_username}'' to Login ... Create new Account If not Created"
            )
        return form_username
