from django.urls import path, include
from django.contrib import admin

from django.views.generic import TemplateView


# Main URLs
urlpatterns = [
    # Core_App
    path('',
         TemplateView.as_view(template_name='Core_App/home.html'),
         name='home-page', ),

    # UserProfile_App
    path('', include('Display_App.urls')),

    # admin panel
    path('admin/', admin.site.urls),
]
