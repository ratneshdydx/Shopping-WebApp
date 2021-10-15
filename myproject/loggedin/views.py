#from django.shortcuts import render,redirect,HttpResponse,reverse
import datetime
#from . models import Notification,Consignment,City
from online.models import Category, Product, LoginInfo
from .cart import Cart
from django.shortcuts import render, get_object_or_404,redirect,reverse,HttpResponse
# Create your views here.
'''def adminhome(request):
    try:
        if request.session['userid']:
            return render(request,'adminhome.html',{'userid':request.session['userid']})
    except KeyError:
        pass
    #return redirect('login')'''

#def product_list(request, category_slug=None):
def adminhome(request, category_slug=None):
    try:
        if request.session['userid']:
            category = None
            categories = Category.objects.all()
            products = Product.objects.filter(available=True)
            if category_slug:
                category = get_object_or_404(Category, slug=category_slug)
                products = Product.objects.filter(category=category,available=True)
            context = {
                'category': category,
                'categories': categories,
                'products': products,
                'userid': request.session['userid']
            }
            return render(request, 'adminhome.html', context)
    except KeyError:
        pass
def product_det(request,id):
    try:
        if request.session['userid']:
            products = get_object_or_404(Product, id=id)
            categories = Category.objects.all()
            price=products.price - (products.price * products.discount)//100
            return render(request, 'product_det.html', {'product':products,'categories':categories,'price':price,'userid':request.session['userid']})
    except KeyError:
        pass

def cart_add(request, product_id):
    try:
        if request.session['userid']:
            cart = Cart(request)  # create a new cart object passing it the request object
            product = get_object_or_404(Product, id=product_id)
    #form = CartAddProductForm(request.POST)
            quantity=request.POST['quantity']

   # if form.is_valid():
        #cd = form.cleaned_data
            cart.add(product=product, quantity=quantity, update_quantity=True)
            return redirect('loggedin:cart_detail')
    except KeyError:
        pass

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('loggedin:cart_detail')


def cart_detail(request):
    try:
        if request.session['userid']:
            cart = Cart(request)
    #'''for item in cart:
    #    item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})'''
            category = None
            categories = Category.objects.all()
            products = Product.objects.filter(available=True)
            sum=cart.get_total_price()
            total_items=cart.__len__()
            total_length=cart.length()
            context = {
                'category': category,
                'categories': categories,
                'products': products,
                'userid': request.session['userid'],
                'cart': cart,
                'sum':sum,
                'total_items':total_items,
                'total_length':total_length
            }
            return render(request, 'cart_detail.html', context)
    except KeyError:
        pass

def logout(request):
    del request.session['userid']
    cart = Cart(request)
    cart.clear()
    return redirect('online:product_list')