from django.conf.urls import patterns, url

from healthy_salad_chooser import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^login/$', views.LoginView.as_view(), name='login'),
	url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
	url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
	url(r'^users/(?P<user>\w+)/$', views.SaladListView.as_view(), name='profile'),
	url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
)
