from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductTest(models.Model):
    size = models.CharField(max_length=20)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User)
