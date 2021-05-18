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

from .pagination import MyCustom_Paginaiton

# ------------------------------------ UsersProfile ------------------------------------
# using ids
# List of UsersProfile


class UsersProfile_ListAPIView(ListAPIView):
    queryset = UsersProfile_Model.objects.all()
    serializer_class = UsersProfile_Serializers
    pagination_class = MyCustom_Paginaiton

    # search_fields = [
    #     'username',
    #     'email',
    #     'display_Name',
    # ]

    filter_fields = [
        'id',

        'username',
        'email',

        'display_Name',
        'profile_Picture',
        'banner_Image',

        'date_joined',
    ]


# using id Retrieve particular UsersProfile
class UsingId_UsersProfiles_RetrieveAPIView(RetrieveAPIView):
    queryset = UsersProfile_Model.objects.all()
    serializer_class = UsersProfile_Serializers


# using username Retrieve particular UsersProfile
class UsingUsername_UsersProfiles_RetrieveAPIView(RetrieveAPIView):
    queryset = UsersProfile_Model.objects.all()
    serializer_class = UsersProfile_Serializers

    def get_object(self, *args, **kwargs):
        return UsersProfile_Model.objects.get(username=self.kwargs.get('UserName_From_URL').lower())


# ------------------------------------ Slices ------------------------------------
# List of Slices
class Slices_ListAPIView(ListAPIView):
    serializer_class = Slices_Serializers
    filter_fields = "__all__"
    pagination_class = MyCustom_Paginaiton

    def get_queryset(self, *args, **kwargs):
        return Slices_Model.objects.filter(visibility='public')


# Retrieve particular Slices
class Slicess_RetrieveAPIView(RetrieveAPIView):
    serializer_class = Slices_Serializers

    def get_queryset(self, *args, **kwargs):
        return Slices_Model.objects.filter(pk=self.kwargs.get('pk'), visibility='public')


# ------------------------------------ Links ------------------------------------
# List of Links
class Links_ListAPIView(ListAPIView):
    serializer_class = Links_Serializers
    filter_fields = "__all__"
    pagination_class = MyCustom_Paginaiton

    def get_queryset(self, *args, **kwargs):
        return Links_Model.objects.filter(visibility='public')


# Retrieve particular Links
class Links_RetrieveAPIView(RetrieveAPIView):
    serializer_class = Links_Serializers

    def get_queryset(self, *args, **kwargs):
        return Links_Model.objects.filter(pk=self.kwargs.get('pk'), visibility='public')
