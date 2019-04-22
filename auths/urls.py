from django.urls import path
from django.conf.urls import url
from .views import user_login, user_logout

urlpatterns = [
    url(r'^login/$', view=user_login, name='user-login'),
    url(r'^logout/$', view=user_logout, name='user-logout'),

]
