from django.db import models

# Create your models here.
class NewsInfo(models.Model):
	#source = models.Integar()
	#format = models.Integar()
	url = models.CharField(max_length=160)
	title = models.CharField(max_length=320)
	imgurl = models.CharField(max_length=160)
	def __unicode__(self):
		return self.title
