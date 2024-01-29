from django.db import models
from django.contrib.auth.models import User
from cadmin.models import House

class User_Req(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    h_id = models.ForeignKey(House, on_delete=models.CASCADE, default=None)
    req_type = models.IntegerField(default=0)
    sharing = models.IntegerField(default=1)
    req_mes = models.CharField(max_length=255, null=True, blank=True)
    req_status = models.BooleanField(default=1)


