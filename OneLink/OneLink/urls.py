from django.urls import path, include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import TemplateView


# Main URLs
urlpatterns = [

    # ADMIN
    path('admin/', admin.site.urls, name='Admin-Page'),

    # CORE
    path('',
         TemplateView.as_view(template_name='Core_App/Home.html'),
         name='Home-Page', ),


    # REGISTRATION
    path('', include('Registration_App.urls')),


    # DISPLAY
    path('<str:UserName_From_URL>/', include('Display_App.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
