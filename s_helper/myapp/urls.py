

from django.conf.urls import url

from . import views


urlpatterns = [
        url(r'^login/$', views.login, name='login'),
        url(r'^register/$', views.register, name='login'),
	url(r'^index/$', views.index,name='index'),
	url(r'^logout/$', views.logout,name='logout'),
	url(r'^upload/$', views.upload,name='upload'),
	url(r'^change_password/$', views.change_password,name='change_password'),
        url(r'^delete/$', views.delete,name='delete'),
        url(r'^delete_deal/$', views.delete_deal,name='delete_deal'),
	url(r'^(?P<itemclass_id>[0-9]+)/$',views.detail,name='detail'),
	
]
