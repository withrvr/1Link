from .models import Slices_Model
from django import forms


# checking if this slice name is allowed to be used or not
def is_slice_name_allowed(self, *args, **kwargs):
    validate_slice_name = self.cleaned_data["slice_Name"]

    import cant_use_this_name
    if validate_slice_name in cant_use_this_name.cant_use_this_name:
        raise forms.ValidationError(
            f"Can't use ''{validate_slice_name}'' as Slice Name - Try Something else"
        )
    return validate_slice_name


# slice list form
class Slices_ListForm(forms.ModelForm):
    class Meta:
        model = Slices_Model
        fields = "__all__"


# slice creation form
class Slices_CreationForm(forms.ModelForm):

    def clean_slice_Name(self, *args, **kwargs):
        return is_slice_name_allowed(self, *args, **kwargs)

    class Meta:
        model = Slices_Model
        fields = ['slice_Name', 'visibility', ]


# slice update form
class Slices_UpdateForm(forms.ModelForm):

    def clean_slice_Name(self, *args, **kwargs):
        return is_slice_name_allowed(self, *args, **kwargs)

    class Meta:
        model = Slices_Model
        fields = ['slice_Name', 'visibility', ]
