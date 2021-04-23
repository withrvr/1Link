from django.urls import path, include
from .views import UsersProfile_UpdateView, UsersProfile_DeleteView


app_name = 'UsersProfile_App'


urlpatterns = [
    path('update/', UsersProfile_UpdateView.as_view(), name='Update-Page'),
    path('delete/', UsersProfile_DeleteView.as_view(), name='Delete-Page'),
]
