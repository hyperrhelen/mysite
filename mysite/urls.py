"""mystie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # User authentication URLS
    url(r'^accounts/login/$', views.login, name="login"),
    # url(r'^accounts/auth/$', include('mysite.views.auth_view')),
    url(r'^accounts/auth/$', views.auth_view, name="auth_view"),
    url(r'^accounts/logout/$', views.logout, name="logout"),
    url(r'^accounts/loggedin/$', views.loggedin,  name="loggedin"),
    url(r'^accounts/invalid/$', views.invalid_login, name="invalid_login"),

    url(r'^accounts/register/$', views.register_user, name="register_user"),
    url(r'^accounts/register_success/$', views.register_success, name="register_success"),


    # url(r'^login/$', login),
    # url(r'^logout/$', logout),
    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'myapp/login.html'}),
    # url(r'^login/$', login_view),
    # url('^', include('django.contrib.auth.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^todo/', include('todo.urls')),
    # url(r'^accounts/login', 'mysite.views.login'),
    # url(r'^login', views.login_view, name='login_view'),
    url(r'^admin/', admin.site.urls),
]