from django.contrib.auth.models import User
from django.db import models
from bs4 import BeautifulSoup
import urllib2

# Create your models here.
class news(models.Model):
	user = models.ForeignKey(User, default=0)
	heading =  models.CharField(max_length=300)
	title = models.CharField(max_length=150,default="title")
	pub_date = models.DateTimeField(auto_now_add=True)
	upvote = models.IntegerField(default=0)

	def __unicode__(self):
		return u'%s' %(self.heading)




