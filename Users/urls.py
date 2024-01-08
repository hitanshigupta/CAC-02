from django.urls import path
from . import views

urlpatterns = [
    path('Users' , views.index , name="index"),
    # path('URL' , views.DEF_NAME , NAME="VAR_NAME"),
]