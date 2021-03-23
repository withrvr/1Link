from django.urls import path

app_name = 'Display_App'

urlpatterns = [
    path('<str:UserName_FromURL>/', ),
    path('<str:UserName_FromURL>/<str:SliceName_FromURL>'),
]
