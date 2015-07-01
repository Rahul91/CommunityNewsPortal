from django.db import models

# Create your models here.
class news(models.Model):
	heading =  models.CharField(max_length=40)
	body = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	upvote = models.IntegerField(default=1)


	def __unicode__(self):
		return u'%s' %(self.heading)

