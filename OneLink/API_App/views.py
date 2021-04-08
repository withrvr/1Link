import django_filters.rest_framework
from django.views.generic import TemplateView

from UsersProfile_App.models import UsersProfile_Model
from Slices_App.models import Slices_Model
from Links_App.models import Links_Model

from .serializers import (
    UsersProfile_Serializers,
    Slices_Serializers,
    Links_Serializers,
)

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)


# ------------------------------------ Home Page ------------------------------------
# home page of api
class API_Home_View(TemplateView):
    template_name = 'API_App/API_Home_Template.html'


# ------------------------------------ UsersProfile ------------------------------------
# List of UsersProfile
class UsersProfile_ListAPIView(ListAPIView):
    queryset = UsersProfile_Model.objects.all()
    serializer_class = UsersProfile_Serializers


# Retrieve particular UsersProfile
class UsersProfiles_RetrieveAPIView(RetrieveAPIView):
    queryset = UsersProfile_Model.objects.all()
    serializer_class = UsersProfile_Serializers


# ------------------------------------ Slices ------------------------------------
# List of Slices
class Slices_ListAPIView(ListAPIView):
    queryset = Slices_Model.objects.all()
    serializer_class = Slices_Serializers


# Retrieve particular Slices
class Slicess_RetrieveAPIView(RetrieveAPIView):
    queryset = Slices_Model.objects.all()
    serializer_class = Slices_Serializers


# ------------------------------------ Links ------------------------------------
# List of Links
class Links_ListAPIView(ListAPIView):
    queryset = Links_Model.objects.all()
    serializer_class = Links_Serializers


# Retrieve particular Links
class Links_RetrieveAPIView(RetrieveAPIView):
    queryset = Links_Model.objects.all()
    serializer_class = Links_Serializers
