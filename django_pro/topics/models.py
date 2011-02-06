from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topics(models.Model):
	topic_name = models.CharField(max_length=200)
	

