from django.db import models
from django.contrib.auth.models import User


class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usertype')
    usertype = models.CharField(max_length=20)


class staff_details(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    staff_email = models.EmailField()
    staff_land_mark = models.CharField(max_length=70, default="Not specified")
    staff_locality = models.CharField(max_length=50, blank=True)
    staff_city = models.CharField(max_length=50, blank=True)
    staff_state = models.CharField(max_length=50, default="Not specified")
    staff_country = models.CharField(max_length=30, default="Not specified")
    staff_pin = models.IntegerField(null=True)
    staff_phone = models.BigIntegerField()
    staff_dob = models.DateField()
    staff_img = models.ImageField(upload_to='images/', null=True, blank=True)
    staff_status = models.BooleanField(default=True)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    flag = models.IntegerField(default=0)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Streets(models.Model):
    Street_name = models.CharField(max_length=100)
    Street_address = models.CharField(max_length=255)
    Street_status = models.BooleanField(default=True)
    Street_image = models.ImageField(upload_to="Streets")


class House(models.Model):
    hs_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    street = models.ForeignKey(Streets, on_delete=models.CASCADE)
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="current_user")
    hs_number = models.CharField(max_length=50, default="Not specified")
    hs_city = models.CharField(max_length=50, default="Lavasa")
    hs_state = models.CharField(max_length=50, default="Maharastra")
    hs_country = models.CharField(max_length=50, default="India")
    hs_pin = models.BigIntegerField(default="412112")
    hs_bhk = models.CharField(max_length=6, default="Not specified")
    hs_rent = models.BigIntegerField(default="0")
    hs_desc = models.TextField(default="Not specified")
    hs_image_1 = models.ImageField(upload_to="House_Images", null=True, blank=True)
    hs_image_2 = models.ImageField(upload_to="House_Images", null=True, blank=True)
    hs_status = models.BooleanField(default=True)


class Contact_Form(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=150)
    ph_no = models.IntegerField()
    message = models.TextField()
