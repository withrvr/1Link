from django.urls import path
from .views import (
    Slices_CreateView,
    Slices_ListView,
    Slices_DetailView_of_Login_User,
)

app_name = 'Slices_App'

urlpatterns = [
    path('', Slices_ListView.as_view(), name='Slices-List-Page'),
    path('new/', Slices_CreateView.as_view(), name='Slices-Create-Page'),
    path(
        '<str:SliceName_From_URL_Of_Login_User>/',
        Slices_DetailView_of_Login_User.as_view(),
        name='Slice-Detail-Page-Of-Login-User'
    ),
]
