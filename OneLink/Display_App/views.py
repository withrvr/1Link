from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from UsersProfile_App.models import UsersProfile_Model


class Users_Detail_View(DetailView):
    model = UsersProfile_Model
    template_name = 'Display_App/Users_Detail_Template.html'
    context_object_name = 'UsersProfile_Object'

    def get_object(self, *args, **kwargs):
        lower_username = self.kwargs.get('UserName_From_URL').lower()
        return get_object_or_404(UsersProfile_Model, username=lower_username)
