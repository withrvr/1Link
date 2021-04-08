from rest_framework import serializers

from UsersProfile_App.models import UsersProfile_Model
from Slices_App.models import Slices_Model
from Links_App.models import Links_Model


# UsersProfile
class UsersProfile_Serializers(serializers.ModelSerializer):
    class Meta:
        model = UsersProfile_Model
        fields = [
            'id',
            'username',
            'email',

            'display_Name',
            'profile_Picture',
            'banner_Image',

            'date_joined',
            'last_login',
        ]


# Slices
class Slices_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Slices_Model
        fields = '__all__'

# Links


class Links_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Links_Model
        exclude = [
            'icon_Image',
            'sub_Name',
        ]
