from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsersProfile_Model


class UsersProfile_CreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UsersProfile_Model
        fields = UserCreationForm.Meta.fields + (
            'username', 'email',
        )
