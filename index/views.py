from django.shortcuts import render_to_response

# Create your views here.
def index(req):
	return render_to_response('index.html',{'user_stylesheet':'css/user.css'})
def baiduhome(req):
	return render_to_response('baidu_homepage.html')

def tencenthome(req):
	return render_to_response('tencent_homepage.html')

def souhuhome(req):
	return render_to_response('souhu_homepage.html')

def neteasyhome(req):
	return render_to_response('neteasy_homepage.html')

def forginhome(req):
	return render_to_response('forgin_homepage.html')
