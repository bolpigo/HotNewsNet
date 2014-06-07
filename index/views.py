from django.shortcuts import render_to_response
from index.models import NewsInfo

# Create your views here.
def index(req):
	newsinfo = NewsInfo.objects.all()
	return render_to_response('index.html',{'newsinfo':newsinfo})
def baiduhome(req):
	newsinfo = NewsInfo.objects.filter(source=0)
	return render_to_response('baidu_homepage.html',{'newsinfo':newsinfo})
def tencenthome(req):
	newsinfo = NewsInfo.objects.filter(source=1)
	return render_to_response('tencent_homepage.html',{'newsinfo':newsinfo})

def souhuhome(req):
	newsinfo = NewsInfo.objects.filter(source=2)
	return render_to_response('souhu_homepage.html',{'newsinfo':newsinfo})

def neteasyhome(req):
	newsinfo = NewsInfo.objects.filter(source=3)
	return render_to_response('neteasy_homepage.html',{'newsinfo':newsinfo})

def forginhome(req):
	return render_to_response('forgin_homepage.html')
