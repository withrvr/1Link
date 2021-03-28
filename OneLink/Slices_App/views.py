from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from UsersProfile_App.mixins import Custom_LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.db import IntegrityError

from .forms import Slices_CreationForm
from django.urls import reverse_lazy, reverse

from django.forms import ValidationError
from django.contrib import messages


# create new user
class Slices_CreateView(Custom_LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'Slices_App/Slices_Create_Template.html'
    success_url = reverse_lazy('Slices_App:Create-Slices-Page')
    form_class = Slices_CreationForm
    # success_message = "Slice was <strong>Created Successfully!!</strong>"

    def form_valid(self, form, *args, **kwargs):
        form.instance.author = validate_user = self.request.user
        validate_slice_Name = form.instance.slice_Name

        try:
            slice_display_url = reverse_lazy('Display_App:Slice-Detail-Page', kwargs={
                'UserName_From_URL': validate_user.username,
                'SliceName_From_URL': validate_slice_Name,
            })
            self.success_message = f'Your Slice <strong>"{validate_slice_Name}"</strong> was Created Successfully!! <a target="_blank" href = "{slice_display_url}">View Created Slice</a>'
            return super().form_valid(form, *args, **kwargs)

        except IntegrityError:
            messages.add_message(
                self.request,
                messages.ERROR,
                f'Slice with Name <strong>"{validate_slice_Name}"</strong> All Ready Exists'
            )
            return HttpResponseRedirect(reverse('Slices_App:Create-Slices-Page'))
