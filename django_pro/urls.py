from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Example:
    # (r'^django_pro/', include('django_pro.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)
