from django.db import models
from django.contrib.auth.models import User
from cadmin.models import House

class User_Req(models.Model):
<<<<<<< HEAD
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    req_type = models.CharField(max_length=20, null=False)
    req_status = models.BooleanField(default=True)
    req_msg = models.TextField(null=True, default="None")
=======
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    h_id = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True)
    req_type = models.IntegerField(default=0)
    req_accept_staff = models.ForeignKey(User, related_name='accept_staff_requests', on_delete=models.CASCADE, null=True, blank=True)
    req_status = models.BooleanField(default=1)


>>>>>>> 30157e4ea137f4d54b7229f6e751d160826cb686
