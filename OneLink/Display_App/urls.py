from django.urls import path
from .views import Users_Detail_View


app_name = 'Display_App'


urlpatterns = [
    # Display Users Info
    path(
        '',
        Users_Detail_View.as_view(),
        name='Users-Detail-Page'
    ),

    # Display Slice Info
    # path('<str:UserName_From_URL>/<str:SliceName_From_URL>/',
    #      name='Slice-Detail-Page'),

]
