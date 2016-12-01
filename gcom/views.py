from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from . import cart
from .models import Product

def home(request):
	try:
		cart.c.lst.append(0)
		cart.c.lst.remove(0)
	except:
		cart.create()
	games=Product.objects.order_by('id')
	return render(request, 'gcom/home.html')

def list(request):
	product_list = Product.objects.order_by('-id')
	product_dictionary = {"Action":[],"Sports":[],"Strategy":[]}
	for i in product_list:
		product_dictionary[i.genre].append(i.id)
	return render(request, "gcom/list.html", {"p_dict" : product_dictionary, "p_list" : product_list})

def product(request, product_id, y_n=0):
	product = get_object_or_404(Product, pk=product_id)
	if y_n==0:
		return render(request, "gcom/gamepage.html", {"product": product})
	else:
		cart.c.add(product.id)
		return render(request, "gcom/gamepage.html", {"product": product})

def xcart(request):
	product_list = cart.c.lst
	for i in range(len(product_list)):
		p_list = get_object_or_404(Product, pk=product_list[i])
	return render(request, "gcom/cartpage.html", {"p_list" : p_list})

def u_cart(request, product_id):
	if product_id!=0:
		c.remove(product_id)
		product_list = c.lst
		for i in range(len(product_list)):
			p_list = get_object_or_404(Product, pk=product_list[i])
		return render(request, "gcom/cartpage.html", {"p_list" : p_list})
	else:
		c.empty_cart()
		return render(request, "gcom/home.html")

def contact(request):
    form_class = ContactForm
    
    return render(request, 'contact.html', {
        'form': form_class,
    })
