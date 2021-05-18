from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse
from django.views.generic import TemplateView, ListView
from django.views.generic.base import RedirectView
from UsersProfile_App.models import UsersProfile_Model
from Slices_App.models import Slices_Model
from django.db.models import Q


class Main_Home_View(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse("Slices_App:Slices-List-Page")
        else:
            return reverse("Core_App:Home-Page")


class Home_View(TemplateView):
    template_name = 'Core_App/Home_Template.html'


class About_View(TemplateView):
    template_name = 'Core_App/About_Template.html'


class Lorem_Ipsum_View(TemplateView):
    template_name = 'Core_App/Lorem_Ipsum_Template.html'


# ------------------------------ ERROR ------------------------------
def Handle_404_Error_View(request, exception=None, *args, **kwargs):
    return render(request, 'Errors_Folder/404_Error_Template.html')


# ------------------------------ ERROR ------------------------------
class Search_Bar_View(TemplateView):
    template_name = 'Core_App/Search_Bar_Template.html'
    context_object_name = 'Search_Result_List'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["search_query"] = search_query = self.request.GET.get('q')
        if search_query:
            context["Users_Search_Result_List"] = UsersProfile_Model.objects.filter(
                Q(username__icontains=search_query) |
                Q(display_Name__icontains=search_query)
            ).order_by('-clicks')
        else:
            context["Users_Search_Result_List"] = UsersProfile_Model.objects.none()

        return context

    def get_queryset(self, *args, **kwargs):
        search_query = self.request.GET.get('q')
        if search_query:
            return UsersProfile_Model.objects.filter(
                Q(username__icontains=search_query) |
                Q(display_Name__icontains=search_query)
            ).order_by('-clicks')
        else:
            return UsersProfile_Model.objects.none()


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
        users = Slices_Model.objects.filter(visibility='public')
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
        if limit > total_number_of_slices:
            limit = total_number_of_slices
        return Slices_Model.objects.filter(visibility='public').order_by("-clicks")[:limit]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Total_Number_Of_Slices"] = Slices_Model.objects.all().count()
        return context
