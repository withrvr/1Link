from django.urls import path
from .views import Slices_CreateView

app_name = 'Slices_App'

urlpatterns = [
    path('new/', Slices_CreateView.as_view(), name='Create-Slices-Page'),
]
