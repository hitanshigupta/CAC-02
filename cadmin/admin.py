from django.contrib import admin
from .models import staff_details
from .models import Notification

admin.site.register(staff_details)
admin.site.register(Notification)

# Register your models here.