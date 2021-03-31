from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.db import IntegrityError
from django.contrib import messages

from django.urls import reverse_lazy, reverse
from django.forms import ValidationError

# from django.views.generic import UpdateView
from django.views.generic import (
    ListView,
    DetailView,

    CreateView,
    UpdateView,
    DeleteView,

    RedirectView,
)

from UsersProfile_App.mixins import Custom_LoginRequiredMixin
from UsersProfile_App.models import UsersProfile_Model

from .forms import Slices_CreationForm, Slices_ListForm, Slices_UpdateForm
from .models import Slices_Model


# ( Redirect's to ) Slices Detail View
class Slices_DetailView_of_Login_User(Custom_LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('Display_App:Slice-Detail-Page', kwargs={
            'UserName_From_URL': self.request.user.username,
            'SliceName_From_URL': self.kwargs.get(
                'SliceName_From_URL'
            )
        })


# list all the slices of the user
class Slices_ListView(Custom_LoginRequiredMixin, ListView):
    template_name = 'Slices_App/Slices_List_Template.html'
    form_class = Slices_ListForm
    context_object_name = 'Slices_List_Object'

    def get_queryset(self, *args, **kwargs):
        return self.request.user.slices_model_set.all()


# create new slice
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


# Update slices info
class Slices_UpdateView(Custom_LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'Slices_App/Slices_Update_Template.html'
    success_url = reverse_lazy('Slices_App:Slices-List-Page')
    form_class = Slices_UpdateForm
    success_message = "Slices Information was <strong>Updated Succesfully</strong>"
    DoesNotExist_error = False

    def get_object(self, *args, **kwargs):
        validate_slice_Name = self.kwargs.get(
            'SliceName_From_URL'
        )
        try:
            return self.request.user.slices_model_set.get(slice_Name=validate_slice_Name)
        except Slices_Model.DoesNotExist:
            messages.add_message(
                self.request,
                messages.WARNING,
                f"No slice with name <strong>''{validate_slice_Name}''</strong> to Update",
            )
            self.DoesNotExist_error = True
            # get_object method only can return object
            # cant return http responce .... throws error

    def dispatch(self, *args, **kwargs):
        dispatch_responce = super().dispatch(*args, **kwargs)
        if self.DoesNotExist_error:
            return HttpResponseRedirect(reverse('Slices_App:Slices-List-Page'))
        return dispatch_responce


# Delete View
class Slices_DeleteView(Custom_LoginRequiredMixin, DeleteView):
    template_name = 'Slices_App/Slices_Delete_Template.html'
    success_url = reverse_lazy('Slices_App:Slices-List-Page')
    model = Slices_Model
    DoesNotExist_error = False

    def get_object(self, *args, **kwargs):
        self.validate_slice_Name = self.kwargs.get(
            'SliceName_From_URL'
        )
        try:
            return self.request.user.slices_model_set.get(slice_Name=self.validate_slice_Name)
        except Slices_Model.DoesNotExist:
            messages.add_message(
                self.request,
                messages.WARNING,
                f"No slice with name <strong>''{self.validate_slice_Name}''</strong> to Delete",
            )
            self.DoesNotExist_error = True
            # get_object method only can return object
            # cant return http responce .... throws error

    def dispatch(self, *args, **kwargs):
        dispatch_responce = super().dispatch(*args, **kwargs)

        if self.DoesNotExist_error:
            return HttpResponseRedirect(reverse('Slices_App:Slices-List-Page'))

        if self.request.method == "POST":
            messages.add_message(
                self.request,
                messages.ERROR,
                f"Slice <strong>''{self.validate_slice_Name}''</strong> was Delete",
            )
        else:
            messages.add_message(
                self.request,
                messages.ERROR,
                f"Are you sure, you want to delete Slice <strong>''{self.validate_slice_Name}''</strong> , All Data accosiated to this Slice will be deleted",
            )

        return dispatch_responce
