from django.contrib import admin
from .models import Links_Model


@admin.register(Links_Model)
class UserProfile_Admin(admin.ModelAdmin):

    # how to show panel ( how to Display )
    list_filter = ('my_Slice', 'visibility', )
    'my_Slice', 'display_Name', 'sub_Name', 'visibility',
    ordering = ('id', 'my_Slice', 'display_Name', 'sub_Name', 'visibility', )
    list_display = (
        'id', 'my_Slice', 'display_Name', 'sub_Name', 'visibility',
    )
    search_fields = (
        'id', 'my_Slice', 'display_Name', 'sub_Name', 'visibility',
    )
