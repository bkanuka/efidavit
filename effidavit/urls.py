from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jumpingintodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^comingsoon/', 'comingsoon.views.index'),
    url(r'^$', 'comingsoon.views.index'),
    # url(r'^admin/', include(admin.site.urls)),
) 

urlpatterns += staticfiles_urlpatterns()
