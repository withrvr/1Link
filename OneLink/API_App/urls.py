from django.views.generic import TemplateView
from django.urls import path
from .views import (

    UsersProfile_ListAPIView,
    UsingId_UsersProfiles_RetrieveAPIView,
    UsingUsername_UsersProfiles_RetrieveAPIView,

    Slices_ListAPIView,
    Slicess_RetrieveAPIView,

    Links_ListAPIView,
    Links_RetrieveAPIView,
)

from rest_framework.schemas import get_schema_view

app_name = 'API_App'


urlpatterns = [

    # default home page for api
    # for now  using Swagger U
    path('', TemplateView.as_view(
        template_name='API_App/swagger-ui.html',
        extra_context={'schema_url': 'API_App:openapi-schema'}
    ), name='API-Home-Page'),

    #     # Documenting API using Swagger UI
    #     path('swagger-ui/', TemplateView.as_view(
    #         template_name='API_App/swagger-ui.html',
    #         extra_context={'schema_url': 'API_App:openapi-schema'}
    #     ), name='swagger-ui'),

    # openapi ( Open API )
    path('openapi', get_schema_view(
        title="1Link API",
        #    description="",
        #    version="1.0.0"
    ), name='openapi-schema'),


    # UsersProfile
    path('users/', UsersProfile_ListAPIView.as_view(),
         name='API-Users-List-Page'),
    path('users/<int:pk>/', UsingId_UsersProfiles_RetrieveAPIView.as_view(),
         name='API-UsingId-Users-Retrieve-Page'),
    path('users/<str:UserName_From_URL>/', UsingUsername_UsersProfiles_RetrieveAPIView.as_view(),
         name='API-UsingUsername-Users-Retrieve-Page'),

    # Slices
    path('slices/', Slices_ListAPIView.as_view(),
         name='API-Slices-List-Page'),
    path('slices/<pk>/', Slicess_RetrieveAPIView.as_view(),
         name='API-Slices-Retrieve-Page'),

    # Links
    path('links/', Links_ListAPIView.as_view(),
         name='API-Links-List-Page'),
    path('links/<pk>/', Links_RetrieveAPIView.as_view(),
         name='API-Links-Retrieve-Page'),
]
