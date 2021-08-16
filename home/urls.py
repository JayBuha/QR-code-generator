from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name='home'),
    path("CreatCode/", views.CreatCode, name="CreatCode"),
    path("save/", views.save, name="save")
]