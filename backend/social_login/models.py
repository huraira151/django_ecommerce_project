from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class VerifyEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.IntegerField()

    def __str__(self):
        return self.user.email
