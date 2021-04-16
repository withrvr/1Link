from django.urls import path, include
from .views import (
    Slices_ListView,
    Slices_DetailView,

    Slices_CreateView,
    Slices_UpdateView,
    Slices_DeleteView,
)

app_name = 'Slices_App'

urlpatterns = [
    path('', Slices_ListView.as_view(), name='Slices-List-Page'),
    path('new/', Slices_CreateView.as_view(), name='Slices-Create-Page'),

    # detail of the
    path(
        '<str:SliceName_From_URL>/',
        Slices_DetailView.as_view(),
        name='Slice-Detail-Page',
    ),

    # Update
    path(
        '<str:SliceName_From_URL>/update/',
        Slices_UpdateView.as_view(),
        name='Slice-Update-Page',
    ),

    # Delete
    path(
        '<str:SliceName_From_URL>/delete/',
        Slices_DeleteView.as_view(),
        name='Slice-Delete-Page',
    ),

    # links operations from this url
    path(
        '<str:SliceName_From_URL>/links/',
        include('Links_App.urls', namespace="Links_App"),
    ),
]
