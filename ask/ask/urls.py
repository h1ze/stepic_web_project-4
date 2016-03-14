from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', 'qa.views.test'),
    url(r'^login/.*$', 'qa.views.test'),
    url(r'^signup/.*$', 'qa.views.test'),
    url(r'^questions/\d+/$', 'qa.views.test'),
    url(r'^ask/.*$', 'qa.views.test'),
    url(r'^popular/.*$', 'qa.views.test'),
    url(r'^new/.*$', 'qa.views.test')
]
