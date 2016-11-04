from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<post_id>[0-9]+)/$', views.single_post, name='single_post'),
]
