from django.db import models

# Create your models here.
class NewsInfo(models.Model):
	source = models.IntegerField() #0,baidu,1,sohu,2,tencent,3,neteasy,3,
	format = models.IntegerField() #has image or not
	url = models.URLField() #url address
	title = models.CharField(max_length=320)#news title
	imgurl = models.URLField()#imgurl address
	imgname = models.CharField(max_length=60)
	content = models.TextField()
	touchTime = models.DateTimeField()
	def __unicode__(self):
		return self.title
