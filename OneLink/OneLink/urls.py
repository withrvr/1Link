from django.urls import path, include
from django.contrib import admin
from django.urls import reverse_lazy

from django.conf.urls.static import static
from django.conf import settings

from django.views.generic.base import TemplateView

from django.contrib.auth.views import PasswordResetConfirmView

# Main URLs
urlpatterns = [

    # Admin Panel
    path('admin-page/', admin.site.urls, name='Admin-Page'),

    # Core (home, about,...)
    path('',
         TemplateView.as_view(template_name='Core_App/Home.html'),
         name='Home-Page', ),


    # Registration ---> login, logout, register  and  password related
    path('', include('Registration_App.urls')),

    # password reset comfirm
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='Registration_App/Users_Password_Reset_Confirm_Template.html',
            success_url=reverse_lazy(
                'Registration_App:password_reset_complete'),
        ),
        name='password_reset_confirm'
    ),


    # UsersProfile ---> update, delete
    path('', include('UsersProfile_App.urls')),


    # Display --> user info, and slice info
    path('<str:UserName_From_URL>/', include('Display_App.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
