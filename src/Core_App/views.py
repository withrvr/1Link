from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from UsersProfile_App.models import UsersProfile_Model
from Slices_App.models import Slices_Model


class Home_View(TemplateView):
    template_name = 'Core_App/Home_Template.html'


class About_View(TemplateView):
    template_name = 'Core_App/About_Template.html'


class Lorem_Ipsum_View(TemplateView):
    template_name = 'Core_App/Lorem_Ipsum_Template.html'

# ------------------------------ RANDOM ------------------------------


# random choice
class Random_Choice_View(TemplateView):
    template_name = 'Core_App/Random_Folder/Random_Choice_Template.html'


# 12 random User
class Random_Users_View(ListView):
    template_name = 'Core_App/Random_Folder/Random_Users_Template.html'
    context_object_name = 'Random_User_List'

    def get_queryset(self, limit=12, *args, **kwargs):
        total_number_of_users = UsersProfile_Model.objects.all().count()

        import random
        users = UsersProfile_Model.objects.all()
        if limit > total_number_of_users:
            limit = total_number_of_users
        return random.sample(list(users), limit)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Total_Number_Of_Users"] = UsersProfile_Model.objects.all().count()
        return context


# 9 random slices
class Random_Slices_View(ListView):
    template_name = 'Core_App/Random_Folder/Random_Slices_Template.html'
    context_object_name = 'Random_Slices_List'

    def get_queryset(self, limit=9, *args, **kwargs):
        total_number_of_slices = Slices_Model.objects.all().count()

        import random
        users = Slices_Model.objects.all()
        if limit > total_number_of_slices:
            limit = total_number_of_slices
        return random.sample(list(users), limit)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Total_Number_Of_Slices"] = Slices_Model.objects.all().count()
        return context


# ------------------------------ POPULAR ------------------------------


# Popular choice
class Popular_Choice_View(TemplateView):
    template_name = 'Core_App/Popular_Folder/Popular_Choice_Template.html'


# Top 10 Users
class Popular_Users_View(ListView):
    template_name = 'Core_App/Popular_Folder/Popular_Users_Template.html'
    context_object_name = 'Popular_User_List'

    def get_queryset(self, limit=10, *args, **kwargs):
        # if users are less that limit
        total_number_of_users = UsersProfile_Model.objects.all().count()
        users = UsersProfile_Model.objects.all()
        if limit > total_number_of_users:
            limit = total_number_of_users

        return UsersProfile_Model.objects.all().order_by("-clicks")[:limit]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Total_Number_Of_Users"] = UsersProfile_Model.objects.all().count()
        return context


# Top 10 Slices
class Popular_Slices_View(ListView):
    template_name = 'Core_App/Popular_Folder/Popular_Slices_Template.html'
    context_object_name = 'Popular_Slices_List'

    def get_queryset(self, limit=10, *args, **kwargs):
        # if slices are less that limit
        total_number_of_slices = Slices_Model.objects.all().count()
        users = Slices_Model.objects.all()
        if limit > total_number_of_slices:
            limit = total_number_of_slices
        return Slices_Model.objects.all().order_by("-clicks")[:limit]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Total_Number_Of_Slices"] = Slices_Model.objects.all().count()
        return context
