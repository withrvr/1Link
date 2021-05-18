from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import DetailView, RedirectView

from UsersProfile_App.models import UsersProfile_Model
from Links_App.models import Links_Model


class Links_Detail_View(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        self.object = get_object_or_404(
            Links_Model,
            id=self.kwargs.get('LinkID_From_URL'),
            visibility='public'
        )

        # increase clicks
        self.object.clicks += 1
        self.object.save()

        return self.object.link_url


class Users_Detail_View(DetailView):
    template_name = 'Display_App/Users_Detail_Template.html'
    context_object_name = 'UsersProfile_Object'
    user_DoesNotExist = False

    def get_object(self, *args, **kwargs):
        lower_username = self.kwargs.get('UserName_From_URL').lower()
        try:
            self.object = UsersProfile_Model.objects.get(
                username=lower_username
            )
            # users clicks ( hits ) count logic
            self.object.clicks += 1
            self.object.save()
        except:
            self.object = UsersProfile_Model.objects.get(
                username='username'
            )
            self.object.username = lower_username
            self.user_DoesNotExist = True
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Slices_List_Object"] = self.object.slices_model_set.filter(
            visibility='public'
        ).order_by('-visibility', '-clicks')
        context["user_DoesNotExist"] = self.user_DoesNotExist
        return context


class Slices_Detail_View(DetailView):
    template_name = 'Display_App/Slices_Detail_Template.html'
    context_object_name = 'Slice_Object'

    def get_object(self, *args, **kwargs):
        lower_username = self.kwargs.get('UserName_From_URL').lower()
        lower_slice_Name = self.kwargs.get('SliceName_From_URL').lower()

        validate_user = get_object_or_404(
            UsersProfile_Model, username=lower_username
        )

        self.object = get_object_or_404(
            validate_user.slices_model_set, slice_Name=lower_slice_Name,
            visibility='public',
        )

        # slices clicks ( hits ) count logic
        self.object.clicks += 1
        self.object.save()

        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Links_List_Object'] = self.object.links_model_set.filter(
            visibility='public'
        )
        return context
