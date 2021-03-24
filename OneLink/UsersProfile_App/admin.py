from .forms import UsersProfile_CreationForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsersProfile_Model


@admin.register(UsersProfile_Model)
class UserProfile_Admin(UserAdmin):

    # forms and model to use
    model = UsersProfile_Model
    add_form = UsersProfile_CreationForm

    # how to show panel ( how to Display )
    list_filter = tuple()
    ordering = ('id', 'username', 'email', )
    list_display = ('username', 'email', 'id',)
    search_fields = UserAdmin.search_fields + ('display_Name', )

    # while creating the user
    # to create the user ... using username and email
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', ),
        }),
    )

    # after user is been created
    # adding extra fields
    fieldsets = (
        ("Extended Fields", {
            'fields': (
                'display_Name',
                'banner_Image',
                'profile_Picture',
            )
        }),
        ("Default User Fields", {'fields': (), }),
        *UserAdmin.fieldsets,
    )
