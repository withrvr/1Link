from django.urls import path, include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import TemplateView


# Main URLs
urlpatterns = [
    # admin panel
    path('admin/', admin.site.urls, name='Admin-Page'),

    # Core_App
    path('',
         TemplateView.as_view(template_name='Core_App/Home.html'),
         name='Home-Page', ),

    # UserProfile_App
    path('', include('Display_App.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
