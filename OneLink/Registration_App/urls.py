from django.urls import path, include
# from django.contrib.auth.urls import urlpatterns

from .views import (
    UsersProfile_CreateView,
    UsersProfile_LoginView,
    UsersProfile_LogoutView,
)


app_name = 'Registration_App'

urlpatterns = [
    path('login/', UsersProfile_LoginView.as_view(), name='Login-Page'),
    path('logout/', UsersProfile_LogoutView.as_view(), name='Logout-Page'),
    path('register/', UsersProfile_CreateView.as_view(), name='Register-Page'),
]
