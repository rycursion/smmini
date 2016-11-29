"""games URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from gcom import views

app_name='gcom'

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', views.home, name="home"),
	url(r'^list/$', views.list, name="list"),
	url(r'^(?P<product_id>[0-9]+)/(?P<y_n>[0-9]+)$', views.product, name="product"),
	url(r'^contact/$', views.contact, name="contact"),
	url(r'^u_cart/(?P<product_id>[0-9]+)$', views.u_cart, name="u_cart"),
]
