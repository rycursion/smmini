from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from . import cart
from .models import Product

def home(request):
	return render(request, 'gcom/home.html')

def list(request):
	product_list = list(Product.objects.order_by('ID').asc())
	product_dictionary = {"action":[],"sports":[],"strategy":[]}
	for i in product_list:
		product_dictionary[i.genre].append(i.ID)
	return render(request, "gcom/list.html", {"p_dict" : product_dictionary, "p_list" : product_list})

def product(request, product_id, y_n):
	product = get_object_or_404(Product, pk=product_id)
	if y_n==0:
		return render(request, "gcom/productpage.html", {"product": product})
	else:
		cart.c.add(product.ID)
		return render(request, "gcom/productpage.html", {"product": product})

def cart(request):
	product_list = cart.c.lst
	for i in range(len(product_list)):
		p_list = get_object_or_404(Product, pk=product_list[i])
	return render(request, "gcom/cartpage.html", {"p_list" : p_list})

def u_cart(request, product_id):
	if product_id!=0:
		cart.c.remove(product_id)
		product_list = cart.c.lst
		for i in range(len(product_list)):
			p_list = get_object_or_404(Product, pk=product_list[i])
		return render(request, "gcom/cartpage.html", {"p_list" : p_list})
	else:
		cart.c.empty_cart()
		return render(request, "gcom/home.html")

def contact(request):
	return render(request, "gcom/contactpage.html")
