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

def sohuhome(req):
	newsinfo = NewsInfo.objects.filter(source=2)
	return render_to_response('sohu_homepage.html',{'newsinfo':newsinfo})

def neteasyhome(req):
	newsinfo = NewsInfo.objects.filter(source=3)
	return render_to_response('neteasy_homepage.html',{'newsinfo':newsinfo})

def forginhome(req):
	return render_to_response('forgin_homepage.html')
def baidumilitary(req):
	newsinfo = NewsInfo.objects.filter(source=0)
	return render_to_response('baidu_military.html',{'newsinfo':newsinfo})
def baiduentertainment(req):
	newsinfo = NewsInfo.objects.filter(source=0)
	return render_to_response('baidu_entertainment.html',{'newsinfo':newsinfo})
def baidutech(req):
	newsinfo = NewsInfo.objects.filter(source=0)
	return render_to_response('baidu_tech.html',{'newsinfo':newsinfo})
def baidusports(req):
	newsinfo = NewsInfo.objects.filter(source=0)
	return render_to_response('baidu_sports.html',{'newsinfo':newsinfo})
def baidusociety(req):
	newsinfo = NewsInfo.objects.filter(source=0)
	return render_to_response('baidu_society.html',{'newsinfo':newsinfo})
def baidueducation(req):
	newsinfo = NewsInfo.objects.filter(source=0)
	return render_to_response('baidu_education.html',{'newsinfo':newsinfo})
def baiduinland(req):
	newsinfo = NewsInfo.objects.filter(source=0)
	return render_to_response('baidu_inland.html',{'newsinfo':newsinfo})
def baiduinternation(req):
	newsinfo = NewsInfo.objects.filter(source=0)
	return render_to_response('baidu_internation.html',{'newsinfo':newsinfo})
def tencentmilitary(req):
	newsinfo = NewsInfo.objects.filter(source=1)
	return render_to_response('tencent_military.html',{'newsinfo':newsinfo})
def tencententertainment(req):
	newsinfo = NewsInfo.objects.filter(source=1)
	return render_to_response('tencent_entertainment.html',{'newsinfo':newsinfo})
def tencenttech(req):
	newsinfo = NewsInfo.objects.filter(source=1)
	return render_to_response('tencent_tech.html',{'newsinfo':newsinfo})
def tencentsports(req):
	newsinfo = NewsInfo.objects.filter(source=1)
	return render_to_response('tencent_sports.html',{'newsinfo':newsinfo})
def tencentsociety(req):
	newsinfo = NewsInfo.objects.filter(source=1)
	return render_to_response('tencent_society.html',{'newsinfo':newsinfo})
def tencentinland(req):
	newsinfo = NewsInfo.objects.filter(source=1)
	return render_to_response('tencent_inland.html',{'newsinfo':newsinfo})
def tencentinternation(req):
	newsinfo = NewsInfo.objects.filter(source=1)
	return render_to_response('tencent_internation.html',{'newsinfo':newsinfo})
def sohumilitary(req):
	newsinfo = NewsInfo.objects.filter(source=2)
	return render_to_response('sohu_military.html',{'newsinfo':newsinfo})
def sohusp_etment(req):
	newsinfo = NewsInfo.objects.filter(source=2)
	return render_to_response('sohu_sp_etment.html',{'newsinfo':newsinfo})
def sohusociety(req):
	newsinfo = NewsInfo.objects.filter(source=2)
	return render_to_response('sohu_society.html',{'newsinfo':newsinfo})
def sohufinance(req):
	newsinfo = NewsInfo.objects.filter(source=2)
	return render_to_response('sohu_finance.html',{'newsinfo':newsinfo})
def sohulife(req):
	newsinfo = NewsInfo.objects.filter(source=2)
	return render_to_response('sohu_life.html',{'newsinfo':newsinfo})
def sohuIT(req):
	newsinfo = NewsInfo.objects.filter(source=2)
	return render_to_response('sohu_IT.html',{'newsinfo':newsinfo})
