from django.urls import path, include
from django.urls import reverse_lazy

from django.views.generic.base import TemplateView, RedirectView

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,

    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from .views import (
    UsersProfile_CreateView,
    UsersProfile_LoginView,
    UsersProfile_LogoutView,
)


app_name = 'Registration_App'


urlpatterns = [

    # users login, logout and create account
    path('login/', UsersProfile_LoginView.as_view(), name='Login-Page'),
    path('logout/', UsersProfile_LogoutView.as_view(), name='Logout-Page'),
    path('register/', UsersProfile_CreateView.as_view(), name='Register-Page'),

    # password reset

    path('password/', RedirectView.as_view(pattern_name='Registration_App:password_reset')),
    path(
        'password-reset/',
        PasswordResetView.as_view(
            template_name='Registration_App/Users_Password_Reset_Template.html',
            success_url=reverse_lazy('Registration_App:password_reset_done'),
        ),
        name='password_reset'
    ),
    path(
        'password-reset-done/',
        PasswordResetDoneView.as_view(
            template_name='Registration_App/Users_Password_Reset_Done_Template.html',
        ),
        name='password_reset_done'
    ),

    # password reset comfirm
    # path(
    #     'password-reset-confirm/<uidb64>/<token>/',
    #     PasswordResetConfirmView.as_view(
    #         template_name='Registration_App/Users_Password_Reset_Confirm_Template.html',
    #         success_url=reverse_lazy(
    #             'Registration_App:password_reset_complete'),
    #     ),
    #     name='password_reset_confirm'
    # ),

    path(
        'password-reset-complete/',
        PasswordResetCompleteView.as_view(
            template_name='Registration_App/Users_Password_Reset_Complete_Template.html'),
        name='password_reset_complete'
    ),
]
