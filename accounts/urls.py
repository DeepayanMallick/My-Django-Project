from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^$', views.home),
	url(r'^message/$', views.message_view, name='message'),
	url(r'^login/$', views.login_view, name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^register/$', views.register_view, name='register'),
	url(r'^profile/$', views.profile_view, name='profile'),
	url(r'^profile/edit/$', views.edit_profile_view, name='profile_edit'),
]