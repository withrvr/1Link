from django.urls import path
from .views import Links_Detail_View, Users_Detail_View, Slices_Detail_View


app_name = 'Display_App'


urlpatterns = [
    # links redirect
    path(
        'links/<int:LinkID_From_URL>/',
        Links_Detail_View.as_view(),
        name='Links-Detail-Page'
    ),

    # Users Info
    path(
        '<str:UserName_From_URL>/',
        Users_Detail_View.as_view(),
        name='Users-Detail-Page'
    ),

    # Slice Info
    path(
        '<str:UserName_From_URL>/<str:SliceName_From_URL>/',
        Slices_Detail_View.as_view(),
        name='Slice-Detail-Page'
    ),

]
