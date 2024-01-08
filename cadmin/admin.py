from django.contrib import admin
from .models import staff_details
from .models import Notification
from .models import UserType

admin.site.register(staff_details)
admin.site.register(Notification)
admin.site.register(UserType)

# Register your models here.