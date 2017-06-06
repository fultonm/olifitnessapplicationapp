"""OliFitnessAppl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

urlpatterns = [
    url(r'^interview/', include('interview.urls')),
    # Although the instructions specify there should be no trailing slash, Google Chrome and other
    # browsers automatically append a slash, resulting in no page being shown. Have both with a
    # slash and no slash routes here, the curl command can work either way.
    url(r'^interview', include('interview.urls')),
    url(r'^admin/', admin.site.urls),
]
