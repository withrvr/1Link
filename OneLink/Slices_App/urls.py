from django.urls import path
from .views import Slices_CreateView, Slices_ListView

app_name = 'Slices_App'

urlpatterns = [
    path('', Slices_ListView.as_view(), name='Slices-List-Page'),
    path('new/', Slices_CreateView.as_view(), name='Slices-Create-Page'),
]
