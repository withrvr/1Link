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
    success_message = "Your Slice was <strong>Created Successfully!!</strong>"

    def form_valid(self, form, *args, **kwargs):
        form.instance.author = validate_user = self.request.user
        try:
            return super().form_valid(form, *args, **kwargs)
        except IntegrityError:
            messages.add_message(
                self.request,
                messages.ERROR,
                f'Slice with Name <strong>"{form.instance.slice_Name}"</strong> All Ready Exists'
            )
            form.add_error(None, f'Slice Name all ready exists')
            return HttpResponseRedirect(reverse('Slices_App:Create-Slices-Page'))
