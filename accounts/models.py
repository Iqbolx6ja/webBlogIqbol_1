from django .contrib.auth.models import AbstracUser
from django.db import models

# Create your models here.
class CustomUser(AbstracUser):
    age = models.PositiveIntegerField(null=True, blank=True)

