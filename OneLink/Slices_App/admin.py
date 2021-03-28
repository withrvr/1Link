from .forms import Slices_CreationForm
from django.contrib import admin
from .models import Slices_Model


@admin.register(Slices_Model)
class UserProfile_Admin(admin.ModelAdmin):

    # how to show panel ( how to Display )
    list_filter = tuple()
    ordering = ('id', 'author', 'visibility', 'slice_Name', )
    list_display = ('id', 'author', 'visibility', 'slice_Name', )
    search_fields = ('id', 'author', 'visibility', 'slice_Name', )
