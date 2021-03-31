from django.urls import path, include

from .views import Links_ListView, Links_UpdateView


app_name = 'Links_App'

urlpatterns = [
    path('', Links_ListView.as_view(), name='Links-List-Page'),


    # Update
    path(
        '<str:LinksID_From_URL>/update/',
        Links_UpdateView.as_view(),
        name='Links-Update-Page',
    ),

]
