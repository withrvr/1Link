from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from UsersProfile_App.models import UsersProfile_Model
from Slices_App.models import Slices_Model


class Users_Detail_View(DetailView):
    model = UsersProfile_Model
    template_name = 'Display_App/Users_Detail_Template.html'
    context_object_name = 'UsersProfile_Object'

    def get_object(self, *args, **kwargs):
        lower_username = self.kwargs.get('UserName_From_URL').lower()
        return get_object_or_404(UsersProfile_Model, username=lower_username)


class Slices_Detail_View(DetailView):
    model = Slices_Model
    template_name = 'Display_App/Slices_Detail_Template.html'
    context_object_name = 'Slice_Object'

    def get_object(self, *args, **kwargs):
        lower_username = self.kwargs.get('UserName_From_URL').lower()
        lower_slice_Name = self.kwargs.get('SliceName_From_URL').lower()

        validate_user = get_object_or_404(
            UsersProfile_Model, username=lower_username
        )

        return get_object_or_404(
            validate_user.slices_model_set, slice_Name=lower_slice_Name,
        )
