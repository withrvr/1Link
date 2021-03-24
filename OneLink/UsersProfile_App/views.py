from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import UsersProfile_ChangeForm
from .models import UsersProfile_Model


# create new user
class UsersProfile_UpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'UsersProfile_App/Users_Update_Template.html'
    success_url = reverse_lazy('UsersProfile_App:Update-Page')
    form_class = UsersProfile_ChangeForm
    success_message = "Your Account was <strong>Updated Successfully!!</strong>"

    def get_object(self, *args, **kwargs):
        return self.request.user
