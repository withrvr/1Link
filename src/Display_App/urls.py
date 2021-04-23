from django.urls import path
from .views import Users_Detail_View, Slices_Detail_View


app_name = 'Display_App'


urlpatterns = [
    # Display Users Info
    path(
        '',
        Users_Detail_View.as_view(),
        name='Users-Detail-Page'
    ),

    # Display Slice Info
    path(
        '<str:SliceName_From_URL>/',
        Slices_Detail_View.as_view(),
        name='Slice-Detail-Page'
    ),

]
