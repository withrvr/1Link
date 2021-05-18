from django.urls import path, include
from django.contrib import admin
from django.urls import reverse_lazy

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.views import PasswordResetConfirmView
from Core_App.views import Handle_404_Error_View

# Main URLs
urlpatterns = [
    # Admin Panel
    path('admin-panel/', admin.site.urls),

    # Core (home, about,...)
    path('', include('Core_App.urls')),


    # Registration ... login, logour, register and password
    path('', include('Registration_App.urls')),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='Registration_App/Users_Password_Reset_Confirm_Template.html',
            success_url=reverse_lazy(
                'Registration_App:password_reset_complete'),
        ),
        name='password_reset_confirm'
    ),


    # dashboard ... UsersProfile and slices
    path('', include('UsersProfile_App.urls')),
    path('slices/', include('Slices_App.urls')),

    # api
    path('api/', include('API_App.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # Display, (user info and slices)
    path('', include('Display_App.urls')),

    path('404/', Handle_404_Error_View, name='404-Page'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = Handle_404_Error_View
