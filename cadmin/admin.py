from django.contrib import admin
from .models import staff_details
from .models import Notification
from .models import UserType
from .models import House

admin.site.register(staff_details)
admin.site.register(Notification)
admin.site.register(UserType)
admin.site.register(House)

# Register your models here.