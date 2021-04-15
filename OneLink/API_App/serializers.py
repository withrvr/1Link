from rest_framework import serializers

from UsersProfile_App.models import UsersProfile_Model
from Slices_App.models import Slices_Model
from Links_App.models import Links_Model
from rest_framework import serializers


# UsersProfile
class UsersProfile_Serializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="API_App:API-UsingId-Users-Retrieve-Page"
    )

    class Meta:
        model = UsersProfile_Model
        fields = [
            'id',
            'url',

            'username',
            'email',

            'display_Name',
            'profile_Picture',
            'banner_Image',

            'date_joined',
            'slices_model_set',
        ]


# Slices
class Slices_Serializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="API_App:API-Slices-Retrieve-Page"
    )

    class Meta:
        model = Slices_Model
        fields = [
            'id',
            'url',
            'author',
            'slice_Name',
            'visibility',
            'links_model_set',
        ]


# Links
class Links_Serializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="API_App:API-Links-Retrieve-Page"
    )

    class Meta:
        model = Links_Model
        fields = [
            'id',
            'url',
            'display_Name',
            'link_url',
            'visibility',
            'my_Slice',
        ]
