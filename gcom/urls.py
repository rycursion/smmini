from django.conf.urls import url,include
from django.contrib import admin
from gcom import views

app_name='gcom'

urlpatterns = [
        url(r'^$', views.home, name="home"),
        url(r'^list/$', views.list, name="list"),
        url(r'^product/(?P<product_id>[0-9]+)/$', views.product, name="product"),
        url(r'^product/(?P<product_id>[0-9]+)/1$', views.product, name="product"),
        url(r'^contact/$', views.contact, name="contact"),
        url(r'^cart/$', views.cart, name='cart'),
        url(r'^u_cart/(?P<product_id>[0-9]+)$', views.u_cart, name="u_cart"),
]

