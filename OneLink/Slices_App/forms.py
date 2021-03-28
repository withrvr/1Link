from .models import Slices_Model
from django import forms


# slice list form
class Slices_ListForm(forms.ModelForm):
    class Meta:
        model = Slices_Model
        fields = "__all__"


# slice creation form
class Slices_CreationForm(forms.ModelForm):

    class Meta:
        model = Slices_Model
        fields = ['slice_Name', 'visibility', ]
