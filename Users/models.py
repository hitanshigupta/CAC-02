from django.db import models
from django.contrib.auth.models import User

class User_Req(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    req_type = models.CharField(max_length=20, null=False)
    req_status = models.BooleanField(default=True)
    req_msg = models.TextField(null=True, default="None")
