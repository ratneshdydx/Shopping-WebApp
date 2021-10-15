from django.shortcuts import render, get_object_or_404,redirect,reverse,HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Category, Product, LoginInfo


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category,available=True)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'index.html', context)

def product_detail(request,id):
    products = get_object_or_404(Product, id=id)
    categories = Category.objects.all()
    price=products.price - (products.price * products.discount)//100
    return render(request, 'product_detail.html', {'product':products,'categories':categories,'price':price})

def validateuser(request):
    userid = request.POST['userid']
    password = request.POST['password']
    try:
        v = LoginInfo.objects.get(userid=userid, password=password)
        if v is not None:
            request.session['userid'] = userid
            return redirect(reverse('loggedin:adminhome'))
            #return HttpResponse("You're logged out.")
    except ObjectDoesNotExist:
        pass

        #return HttpResponse("Please Enter Right Password")
    return redirect('online:product_list')

