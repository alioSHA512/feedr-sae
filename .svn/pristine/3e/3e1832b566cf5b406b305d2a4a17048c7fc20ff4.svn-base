from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# from formobile import urls


urlpatterns = patterns ('',
    # Examples:
    # url(r'^$', 'feedr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^formobile/', include('formobile.urls')),
)