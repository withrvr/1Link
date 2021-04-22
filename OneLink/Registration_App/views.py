from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect

from UsersProfile_App.forms import UsersProfile_CreationForm
from UsersProfile_App.models import UsersProfile_Model

from django.urls import reverse, reverse_lazy

from django.views.generic.edit import CreateView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

# for form_valid method
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login

from .forms import Users_Login_AuthenticationForm


# create new user
class UsersProfile_CreateView(SuccessMessageMixin, CreateView):
    template_name = 'Registration_App/Users_Register_Template.html'
    success_url = reverse_lazy('Registration_App:Login-Page')
    form_class = UsersProfile_CreationForm
    success_message = "Your Account was <strong>Created Successfully!!</strong>"

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        current_user = request.user
        if request.method == "GET":
            # if is_authenticated and trying to Register account ... then redirect
            if current_user.is_authenticated:
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    f'You have Register and Login with <strong>"@{current_user.username}"</strong> account'
                )
                return HttpResponseRedirect(reverse('Core_App:Home-Page'))

            else:
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Filling up this Information, <b>And Create The brand new Account</b>'
                )

        return response


# login user
class UsersProfile_LoginView(SuccessMessageMixin, LoginView):
    template_name = 'Registration_App/Users_Login_Template.html'
    success_message = 'You have <strong>Login</strong> succesfully !!!'
    form_class = Users_Login_AuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        current_user = request.user

        if request.method == "GET":
            # if is_authenticated and trying again to login ... then redirect
            if current_user.is_authenticated:
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    f'You are currently Login with <strong>"@{current_user.username}"</strong> account'
                )
                return HttpResponseRedirect(reverse('Core_App:Home-Page'))

            else:
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    f"You are currently <strong>Not Login</strong> with any Account"
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
