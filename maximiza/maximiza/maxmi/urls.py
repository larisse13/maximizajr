from django.conf.urls import url, include, patterns

urlpatterns = patterns('maximiza.maxmi.views',
	url(r'^$', 'home', name='home'),   
)