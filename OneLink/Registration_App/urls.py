from django.urls import path, include
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)


app_name = 'Registration_App'

urlpatterns = [

    path('login/', LoginView.as_view(
        template_name='Registration_App/Users_Login_Template.html'), name='Login-Page'),
    path('logout/', LogoutView.as_view(
        template_name='Registration_App/Users_Logout_Template.html'), name='Logout-Page'),

]
