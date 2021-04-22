from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from UsersProfile_App.models import UsersProfile_Model


class Home_View(TemplateView):
    template_name = 'Core_App/Home_Template.html'


class Random_Users_View(TemplateView):
    template_name = 'Core_App/Random_Users_Template.html'

    def generate_Random_Users_List(self, limit=12, *args, **kwargs):
        total_number_of_users = UsersProfile_Model.objects.all().count()

        import random
        users = UsersProfile_Model.objects.all()
        if limit > total_number_of_users:
            limit = total_number_of_users
        return random.sample(list(users), limit)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Random_User_List"] = self.generate_Random_Users_List()
        context["total_number_of_users"] = UsersProfile_Model.objects.all().count()
        return context
