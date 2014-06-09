from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HotNewsNet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^index$','index.views.index'),
    url(r'^nbhome$','index.views.baiduhome'), 
    url(r'^nthome$','index.views.tencenthome'),
    url(r'^nshome$','index.views.souhuhome'),
    url(r'^nnhome$','index.views.neteasyhome'),
    url(r'^nfhome$','index.views.forginhome'),
    url(r'^$','index.views.index'),
    url(r'^nbmilitary$','index.views.baidumilitary'), 
    url(r'^nbentertainment$','index.views.baiduentertainment'), 
    url(r'^nbtech$','index.views.baidutech'), 
    url(r'^nbsports$','index.views.baidusports'), 
    url(r'^nbsociety$','index.views.baidusociety'), 
    url(r'^nbeducation$','index.views.baidueducation'), 
    url(r'^nbinland$','index.views.baiduinland'), 
    url(r'^nbinternation$','index.views.baiduinternation'), 
    url(r'^ntmilitary$','index.views.tencentmilitary'), 
    url(r'^ntentertainment$','index.views.tencententertainment'), 
    url(r'^nttech$','index.views.tencenttech'), 
    url(r'^ntsports$','index.views.tencentsports'), 
    url(r'^ntsociety$','index.views.tencentsociety'), 
    url(r'^ntinland$','index.views.tencentinland'), 
    url(r'^ntinternation$','index.views.tencentinternation'), 
    url(r'^nsmilitary$','index.views.sohumilitary'), 
    url(r'^nssp_etment$','index.views.sohusp_etment'), 
    url(r'^nssociety$','index.views.sohusociety'), 
    url(r'^nsfinance$','index.views.sohufinance'), 
    url(r'^nslife$','index.views.sohulife'), 
    url(r'^nsIT$','index.views.IT'), 
    # url(r'^static/(?P<path>.*)','django.views.static.serve',{'document_root':'e:/pythonproject/HotNewsNet/index/static'}),

)
