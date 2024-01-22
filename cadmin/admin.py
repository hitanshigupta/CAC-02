from django.contrib import admin
from .models import staff_details
from .models import Notification
from .models import UserType
from .models import House
from .models import h_img

admin.site.register(staff_details)
admin.site.register(Notification)
admin.site.register(UserType)
admin.site.register(House)
admin.site.register(h_img)

# Register your models here.