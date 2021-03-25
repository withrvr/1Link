from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages

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


# delete user
class UsersProfile_DeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'UsersProfile_App/Users_Delete_Template.html'
    success_url = reverse_lazy('Registration_App:Login-Page')
    model = UsersProfile_Model

    def get_object(self, *args, **kwargs):
        messages.add_message(
            self.request, messages.ERROR,
            'Make Sure before deleteing the account <strong>All the data will be lost</strong>'
        )
        messages.add_message(
            self.request, messages.ERROR,
            '<strong>Slices and Links Also</strong> which have been shared all over the internet'
        )
        return self.request.user
