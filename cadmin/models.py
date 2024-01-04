from django.db import models
from django.contrib.auth.models import User

class staff_details(models.Model):
    user_id = models.IntegerField()
    staff_email = models.EmailField()
    staff_land_mark = models.CharField(max_length = 70 , default = "Not specified")
    staff_locality = models.CharField(max_length = 50 , blank = True)
    staff_city = models.CharField(max_length = 50 , blank = True)
    staff_state = models.CharField(max_length = 50 , default = "Not specified")
    staff_country = models.CharField(max_length = 30 , default = "Not specified")
    staff_pin = models.IntegerField(null = True)
    staff_phone = models.BigIntegerField()
    staff_dob = models.DateField()
    staff_img = models.ImageField(upload_to='images/' , null=True)
    staff_status = models.BooleanField(default=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

