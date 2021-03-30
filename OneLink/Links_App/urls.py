from django.urls import path, include

from .views import Links_ListView


app_name = 'Links_App'

urlpatterns = [
    path('', Links_ListView.as_view(), name='Links-List-Page'),

]
