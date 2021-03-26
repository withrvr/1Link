from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect

from UsersProfile_App.forms import UsersProfile_CreationForm
from UsersProfile_App.models import UsersProfile_Model


from django.views.generic.edit import CreateView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)


# create new user
class UsersProfile_CreateView(SuccessMessageMixin, CreateView):
    template_name = 'Registration_App/Users_Register_Template.html'
    success_url = reverse_lazy('Registration_App:Login-Page')
    form_class = UsersProfile_CreationForm
    success_message = "Your Account was <strong>Created Successfully!!</strong>"

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if request.method == "GET":
            messages.add_message(
                request,
                messages.SUCCESS,
                'Filling up this Information, <b>And Create the brand new Account</b>'
            )
        return response


# login user
class UsersProfile_LoginView(SuccessMessageMixin, LoginView):
    template_name = 'Registration_App/Users_Login_Template.html'
    success_message = 'You have <strong>Login</strong> succesfully !!!'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if request.method == "GET":
            messages.add_message(
                request,
                messages.SUCCESS,
                '<strong>Login</strong> to your Account'
            )
        return response


# logout user
class UsersProfile_LogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(
            request,
            messages.ERROR,
            'You have been <strong>Logged out !!!</strong>',
        )
        return redirect('Registration_App:Login-Page')
