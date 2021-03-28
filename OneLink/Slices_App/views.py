from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from UsersProfile_App.mixins import Custom_LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.db import IntegrityError
from django.urls import reverse_lazy, reverse
from django.forms import ValidationError
from django.contrib import messages

from .forms import Slices_CreationForm, Slices_ListForm
from .models import Slices_Model
from UsersProfile_App.models import UsersProfile_Model

# list all the slices of the user


class Slices_ListView(Custom_LoginRequiredMixin, ListView):
    model = Slices_Model
    template_name = 'Slices_App/Slices_List_Template.html'
    success_url = reverse_lazy('Slices_App:Slices-Create-Page')
    form_class = Slices_ListForm
    context_object_name = 'Slices_List_Object'

    def get_queryset(self, *args, **kwargs):
        return self.request.user.slices_model_set.all()


# create new user
class Slices_CreateView(Custom_LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'Slices_App/Slices_Create_Template.html'
    success_url = reverse_lazy('Slices_App:Slices-Create-Page')
    form_class = Slices_CreationForm

    def form_valid(self, form, *args, **kwargs):
        # whenever slice is created add author as the login user
        form.instance.author = validate_user = self.request.user
        validate_slice_Name = form.instance.slice_Name

        try:
            slice_display_url = reverse_lazy('Display_App:Slice-Detail-Page', kwargs={
                'UserName_From_URL': validate_user.username,
                'SliceName_From_URL': validate_slice_Name,
            })
            self.success_message = f'Your Slice <strong>"{validate_slice_Name}"</strong> was Created Successfully!! <a target="_blank" href = "{slice_display_url}">View Created Slice</a>'

            # IntegrityError will come here if slice name is already exists
            return super().form_valid(form, *args, **kwargs)

        except IntegrityError:
            messages.add_message(
                self.request,
                messages.ERROR,
                f'Slice with Name <strong>"{validate_slice_Name}"</strong> Already Exists'
            )
            return HttpResponseRedirect(reverse('Slices_App:Slices-Create-Page'))
