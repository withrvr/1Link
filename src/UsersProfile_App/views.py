from django.shortcuts import render
from django.views.generic import (
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages

from .mixins import Custom_LoginRequiredMixin
from .forms import UsersProfile_ChangeForm
from .models import UsersProfile_Model


# self info ( users detail )
class UsersProfile_DetailView(Custom_LoginRequiredMixin, DetailView):
    template_name = 'UsersProfile_App/Users_Detail_Template.html'
    context_object_name = 'UsersProfile_Object'

    def get_object(self, *args, **kwargs):
        return self.request.user


# create new user
class UsersProfile_UpdateView(Custom_LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'UsersProfile_App/Users_Update_Template.html'
    success_url = reverse_lazy('UsersProfile_App:Self-Info-Page')
    form_class = UsersProfile_ChangeForm
    success_message = "Your Account was <strong>Updated Successfully!!</strong>"

    def get_object(self, *args, **kwargs):
        return self.request.user

    def dispatch(self, *args, **kwargs):
        if self.request.method == "GET":
            messages.add_message(
                self.request,
                messages.SUCCESS,
                '<strong>Update</strong> your Account Again, If needed'
            )
        return super().dispatch(self.request, *args, **kwargs)


# delete user
class UsersProfile_DeleteView(Custom_LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'UsersProfile_App/Users_Delete_Template.html'
    success_url = reverse_lazy('Registration_App:Login-Page')
    model = UsersProfile_Model

    def get_object(self, *args, **kwargs):
        return self.request.user

    def dispatch(self, *args, **kwargs):
        if self.request.method == "GET":
            messages.add_message(
                self.request, messages.ERROR,
                'Make Sure before deleteing the account <strong>All the data will be lost</strong>'
            )
            messages.add_message(
                self.request, messages.ERROR,
                '<strong>Slices and Links Also</strong> which have been shared all over the internet'
            )
        else:
            messages.add_message(
                self.request, messages.ERROR,
                'Your Account was <strong>Deleted !!!</strong>'
            )

        return super().dispatch(self.request, *args, **kwargs)
