"""frc_scout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from frc_scout import views
from api import teams

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    # Home
	url(r'^$', views.home),

    # Pre Event
    url(r'^setup/$', views.setup),
    url(r'^api/addteam/$', teams.add_team),

    # Match Scout
	url(r'^scout/$', views.scout),
    url(r'^scout/config/$', views.scout_config),
    url(r'^scout/auto/$', views.scout_auto),

    # Data Analysis
	url(r'^data/$', views.data)

]
