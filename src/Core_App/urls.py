from django.urls import path
from django.views.generic.base import RedirectView

from .views import (
    Home_View,

    # random
    Random_Choice_View,
    Random_Users_View,
    Random_Slices_View,

    # Popular
    Popular_Choice_View,
    Popular_Users_View,
    Popular_Slices_View,
)

app_name = 'Core_App'

urlpatterns = [
    # home page
    path('', Home_View.as_view(), name='Home-Page', ),
    path('home/', RedirectView.as_view(pattern_name='Core_App:Home-Page')),

    # Random Users & Slices
    path('random/', Random_Choice_View.as_view(), name='Random-Choice-Page'),
    path('random/users/', Random_Users_View.as_view(), name='Random-Users-Page'),
    path('random/slices/', Random_Slices_View.as_view(), name='Random-Slices-Page'),

    # Popular Users & Slices
    path('popular/', Popular_Choice_View.as_view(), name='Popular-Choice-Page'),
    path('popular/users/', Popular_Users_View.as_view(), name='Popular-Users-Page'),
    path('popular/slices/', Popular_Slices_View.as_view(),
         name='Popular-Slices-Page'),
]
