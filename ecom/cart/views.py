from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    #Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities})

def cart_add(request):
    #Get the cart
    cart = Cart(request)
    # Test the POST
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        #product quantity
        product_qty = int(request.POST.get('product_qty'))
        # Lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        #Save to session
        cart.add(product=product, quantity=product_qty)
        #Get Cart Quantity
        cart_quantity = cart.__len__()
        #Return response
       #response = JsonResponse({'Product Name:': product.name})
        #return response
        response = JsonResponse({'qty:': cart_quantity})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass
