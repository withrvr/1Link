from .models import Links_Model
from django import forms


# Links list form
class Links_ListForm(forms.ModelForm):
    class Meta:
        model = Links_Model
        fields = "__all__"


# Link update form
class Links_UpdateForm(forms.ModelForm):
    class Meta:
        model = Links_Model
        exclude = ('my_Slice', 'icon_Image', 'sub_Name',)


# Link create form
class Links_CreateForm(forms.ModelForm):
    class Meta:
        model = Links_Model
        exclude = ('my_Slice', 'icon_Image', 'sub_Name',)
