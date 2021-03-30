from django.shortcuts import render
from django.views.generic import ListView

from UsersProfile_App.mixins import Custom_LoginRequiredMixin
from .models import Links_Model
from .forms import Slices_ListForm


# list all the slices of the user
class Links_ListView(Custom_LoginRequiredMixin, ListView):
    model = Links_Model
    template_name = 'Links_App/Links_List_Template.html'
    form_class = Slices_ListForm
    context_object_name = 'Links_List_Object'

    def get_queryset(self, *args, **kwargs):
        validate_my_slice = self.request.user.slices_model_set.get(slice_Name=self.kwargs.get(
            'SliceName_From_URL_Of_Login_User'
        ))
        return validate_my_slice.links_model_set.all()
