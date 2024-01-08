from django.urls import path
from . import views

urlpatterns = [
    path('users' , views.index , name="users"),
    # path('URL' , views.DEF_NAME , NAME="VAR_NAME"),
]