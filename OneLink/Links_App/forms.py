from .models import Links_Model
from django import forms


# slice list form
class Slices_ListForm(forms.ModelForm):
    class Meta:
        model = Links_Model
        fields = "__all__"
