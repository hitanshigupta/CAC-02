from django.db import models
from django.contrib.auth.models import User
from cadmin.models import House

class User_Req(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    h_id = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True)
    req_type = models.IntegerField(default=0)
    req_accept_staff = models.ForeignKey(User, related_name='accept_staff_requests', on_delete=models.CASCADE, null=True, blank=True)
    req_status = models.BooleanField(default=1)


