from django.shortcuts import render
from .models import *

def home(request):
    
    if "product" in request.GET:
        product_query = request.GET['product']
        products=Product.objects.filter(name__icontains=product_query)
        context={"Products":products}

    else:
        products=Product.objects.all()
        context={"Products":products}
    
    return render(request, "app001/products.html", context)
