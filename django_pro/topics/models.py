from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Admin:
	list_display = ('author','date')
class Topics(models.Model):
	topic_name = models.CharField(max_length=200)
	image_url = models.CharField(max_length=100)
	topic_guid = models.CharField(max_length=100)
 
class Posts(models.Model):
	author = models.ForeignKey(User)
	date = models.DateTimeField()
	title = models.CharField(max_length=100)
	post = models.TextField()
	
	

