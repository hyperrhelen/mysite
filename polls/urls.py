from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # url(r'^$', views.my_view, name='my_view'),
    # url(r'^$', views.logout_view, name='logout_view'),
    # url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]