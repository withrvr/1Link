from django.urls import path, include
from .views import UsersProfile_UpdateView


app_name = 'UsersProfile_App'


urlpatterns = [
    path('update/', UsersProfile_UpdateView.as_view(), name='Update-Page'),
]
