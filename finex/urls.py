from django.conf.urls import patterns, include, url

# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'finex.views.home',name='home'),
    url(r'^login/$', 'finex.views.login_user',name='login'),
    url(r'^logout/$', 'finex.views.logout_user',name='logout'),
)