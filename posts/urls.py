from django.conf.urls import include
from django.urls import path
from .views import post_create, post_detail, add_comment
from django.conf.urls import url

urlpatterns = [
    url(r'^post-create/$', post_create, name='post-create'),
    url(r'^post-detail/(?P<slug>[-\w]+)/$', post_detail, name='post-detail'),
    url(r'^add-comment/(?P<slug>[-\w]+)/$', add_comment, name='add-comment'),

]
