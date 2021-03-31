from django.urls import path, include

from .views import Links_ListView, Links_UpdateView, Links_DeleteView


app_name = 'Links_App'

urlpatterns = [
    path('', Links_ListView.as_view(), name='Links-List-Page'),


    # Update link
    path(
        '<str:LinksID_From_URL>/update/',
        Links_UpdateView.as_view(),
        name='Links-Update-Page',
    ),

    # Delete link
    path(
        '<str:LinksID_From_URL>/delete/',
        Links_DeleteView.as_view(),
        name='Links-Delete-Page',
    ),
]
