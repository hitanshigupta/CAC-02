from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name="index"),
    # path('URL' , views.DEF_NAME , NAME="VAR_NAME"),
]