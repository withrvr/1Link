from django.urls import path
from django.views.generic.base import RedirectView

from .views import Home_View, Random_Users_View, Random_Slices_View
app_name = 'Core_App'

urlpatterns = [
    # home page
    path('', Home_View.as_view(), name='Home-Page', ),
    path('home/', RedirectView.as_view(pattern_name='Core_App:Home-Page')),

    # Random Users, Slices
    path('random-users/', Random_Users_View.as_view(), name='Random-Users-Page'),
    path('random-slices/', Random_Slices_View.as_view(), name='Random-Slices-Page'),
]
