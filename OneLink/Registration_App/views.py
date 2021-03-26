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
    success_message = "Your Account was <strong>Created Successfully!!</strong> ... To Continue <strong>Login</strong> into Your Account"


# login user
class UsersProfile_LoginView(SuccessMessageMixin, LoginView):
    template_name = 'Registration_App/Users_Login_Template.html'
    success_message = 'You have <strong>Login</strong> succesfully !!!'


# logout user
class UsersProfile_LogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(
            request,
            messages.ERROR,
            'You have been Logged out !!! <strong>Log in Again</strong>',
        )
        return redirect('Registration_App:Login-Page')
