from django.urls import path
from django.views.generic.base import RedirectView

from .views import (
    # random
    Random_Choice_View,
    Random_Users_View,
    Random_Slices_View,

    # Popular
    Popular_Choice_View,
    Popular_Users_View,
    Popular_Slices_View,

    # other
    Main_Home_View,
    Home_View,
    About_View,

    Lorem_Ipsum_View,
    Search_Bar_View,
)

app_name = 'Core_App'

urlpatterns = [
    # home page
    path('', Main_Home_View.as_view(), name='Main-Home-Page'),
    path('home/', Home_View.as_view(), name='Home-Page'),
    path('about/', About_View.as_view(), name='About-Page'),
    path('search/', Search_Bar_View.as_view(), name='Search-Bar-Page'),

    # Random Users & Slices
    path('random/', Random_Choice_View.as_view(), name='Random-Choice-Page'),
    path('random/users/', Random_Users_View.as_view(), name='Random-Users-Page'),
    path('random/slices/', Random_Slices_View.as_view(), name='Random-Slices-Page'),

    # Popular Users & Slices
    path('popular/', Popular_Choice_View.as_view(), name='Popular-Choice-Page'),
    path('popular/users/', Popular_Users_View.as_view(), name='Popular-Users-Page'),
    path('popular/slices/', Popular_Slices_View.as_view(),
         name='Popular-Slices-Page'),

    # lorem ipsum
    path('lorem/', Lorem_Ipsum_View.as_view(), name='Lorem-Ipsum-Page'),
    path('ipsum/', Lorem_Ipsum_View.as_view()),
    path('loremipsum/', Lorem_Ipsum_View.as_view()),
    path('lorem-ipsum/', Lorem_Ipsum_View.as_view()),

]
