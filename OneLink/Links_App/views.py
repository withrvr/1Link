from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
)

from UsersProfile_App.mixins import Custom_LoginRequiredMixin
from .models import Links_Model
from .forms import (
    Links_ListForm,
    Links_UpdateForm,
    Links_CreateForm,
)


# create link
class Links_CreateView(Custom_LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'Links_App/Links_Create_Template.html'
    form_class = Links_CreateForm
    context_object_name = 'Links_Object'
    success_message = "Links was <strong>Created Succesfully</strong>"
    DoesNotExist_error = False

    def get_success_url(self, *args, **kwargs):
        return reverse('Slices_App:Links_App:Links-List-Page', kwargs={
            'SliceName_From_URL': self.kwargs.get(
                'SliceName_From_URL'
            )
        })

    def form_valid(self, form, *args, **kwargs):
        # whenever link is created add slice name automatically
        form.instance.my_Slice = self.request.user.slices_model_set.get(slice_Name=self.kwargs.get(
            'SliceName_From_URL'
        ))
        return super().form_valid(form, *args, **kwargs)


# list all the slices of the user
class Links_ListView(Custom_LoginRequiredMixin, ListView):
    template_name = 'Links_App/Links_List_Template.html'
    form_class = Links_ListForm
    context_object_name = 'Links_List_Object'

    def get_queryset(self, *args, **kwargs):
        validate_my_slice = self.request.user.slices_model_set.get(slice_Name=self.kwargs.get(
            'SliceName_From_URL'
        ))
        return validate_my_slice.links_model_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_Slice_Name'] = self.kwargs.get(
            'SliceName_From_URL'
        )
        return context


# update links
class Links_UpdateView(Custom_LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'Links_App/Links_Update_Template.html'
    form_class = Links_UpdateForm
    context_object_name = 'Links_Object'
    success_message = "Links Info was <strong>Updated Succesfully</strong>"
    DoesNotExist_error = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_Slice_Name'] = self.kwargs.get(
            'SliceName_From_URL'
        )
        context['current_Link_Id'] = self.kwargs.get(
            'LinksID_From_URL'
        )
        return context

    def get_success_url(self, *args, **kwargs):
        return reverse('Slices_App:Links_App:Links-List-Page', kwargs={
            'SliceName_From_URL': self.kwargs.get(
                'SliceName_From_URL'
            )
        })

    def get_object(self, *args, **kwargs):
        validate_my_slice = self.request.user.slices_model_set.get(slice_Name=self.kwargs.get(
            'SliceName_From_URL'
        ))
        validate_links_ID = self.kwargs.get(
            'LinksID_From_URL'
        )
        try:
            return validate_my_slice.links_model_set.get(id=validate_links_ID)
        except Links_Model.DoesNotExist:
            messages.add_message(
                self.request,
                messages.WARNING,
                f"No Link with id number <strong>''{validate_links_ID}''</strong> to Update",
            )
            self.DoesNotExist_error = True
            # get_object method only can return object
            # cant return http responce .... throws error

    def dispatch(self, *args, **kwargs):
        dispatch_responce = super().dispatch(*args, **kwargs)
        if self.DoesNotExist_error:
            return HttpResponseRedirect(reverse('Slices_App:Links_App:Links-List-Page', kwargs={
                'SliceName_From_URL': self.kwargs.get(
                    'SliceName_From_URL'
                )
            }))
        return dispatch_responce


# Delete View
class Links_DeleteView(Custom_LoginRequiredMixin, DeleteView):
    template_name = 'Links_App/Links_Delete_Template.html'
    model = Links_Model
    DoesNotExist_error = False

    def get_success_url(self, *args, **kwargs):
        return reverse('Slices_App:Links_App:Links-List-Page', kwargs={
            'SliceName_From_URL': self.kwargs.get(
                'SliceName_From_URL'
            )
        })

    def get_object(self, *args, **kwargs):
        self.validate_my_slice = self.request.user.slices_model_set.get(slice_Name=self.kwargs.get(
            'SliceName_From_URL'
        ))
        validate_links_ID = self.kwargs.get(
            'LinksID_From_URL'
        )
        try:
            return self.validate_my_slice.links_model_set.get(id=validate_links_ID)
        except Links_Model.DoesNotExist:
            messages.add_message(
                self.request,
                messages.WARNING,
                f"No Link with id number <strong>''{validate_links_ID}''</strong> to Delete",
            )
            self.DoesNotExist_error = True
            # get_object method only can return object
            # cant return http responce .... throws error

    def dispatch(self, *args, **kwargs):
        dispatch_responce = super().dispatch(*args, **kwargs)

        if self.DoesNotExist_error:
            return HttpResponseRedirect(reverse('Slices_App:Links_App:Links-List-Page', kwargs={
                'SliceName_From_URL': self.kwargs.get(
                    'SliceName_From_URL'
                )
            }))

        if self.request.method == "POST":
            messages.add_message(
                self.request,
                messages.ERROR,
                f"Link was Deleted",
            )
        else:
            messages.add_message(
                self.request,
                messages.ERROR,
                f'Are you sure, you want to delete Link, All Data accosiated to this Link will be deleted<br>'
            )

        return dispatch_responce
