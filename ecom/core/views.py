from django.shortcuts import render,redirect
from core.models import Slider,BannerArea,MainCategory,Product,UpcomingProduct,Blog,Category,Color,Brand
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Max, Min



def Base(request):
    return render(request, 'base.html')

def AboutUs(request):
    return render(request, 'main/about.html')

def ContactUs(request):
    return render(request, 'main/contact.html')

def Faq(request):
    return render(request, 'main/faq.html')

def BlogView(request):
    blog = Blog.objects.all()
    blogs = Blog.objects.filter(section__name = 'Popular Feeds')
    newblogs = Blog.objects.filter(section__name = 'New Blog')

    context ={
        'blog' : blog,
        'blogs' : blogs,
        'newblogs' : newblogs,
    }
    return render(request, 'main/blog.html', context)

def BlogDetail(request,slug):
    blog = Blog.objects.filter(slug = slug)

    if blog.exists():
        blog = Blog.objects.get(slug = slug)
    else:
        return redirect('404')
        
    context = {
        'blog' : blog,
    }
    return render(request, 'main/blog_detail.html', context)





def Home(request):
    sliders = Slider.objects.all()
    banners = BannerArea.objects.all()
    main_category = MainCategory.objects.all()
    product = Product.objects.filter(section__name = 'Top Deals Of The Day')
    products = Product.objects.filter(section__name = 'Top Featured Products')
    up_products = UpcomingProduct.objects.filter(section__name = 'New & Upcoming')
    
    context = {
        'sliders' : sliders,
        'banners' : banners,
        'main_category' : main_category,
        'product' : product,
        'products' : products,
        'up_products' : up_products
    }
    return render(request, 'main/home.html', context)


def Shop(request):
    category = Category.objects.all()
    product = Product.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    products = Product.objects.filter(section__name = 'Top Featured Products')

    min_price = Product.objects.all().aggregate(Min('price'))
    max_price = Product.objects.all().aggregate(Max('price'))
    ColorID = request.GET.get('ColorID')

    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:
        Int_FilterPrice = int(FilterPrice)
        product = Product.objects.filter(price__lte = Int_FilterPrice)
        print(product)
    elif ColorID:
        product = Product.objects.filter(color = ColorID)
    
    else:
        product = Product.objects.all()
    

    context = {
        'category' : category,
        'product' : product,
        'min_price' : min_price,
        'max_price' : max_price,
        'FilterPrice' : FilterPrice,
        'color' : color, 
        'brand' : brand,   
        'products' : products,
    }

    return render(request, 'product/shop.html', context)

def filter_data(request):
    categories = request.GET.getlist('category[]')
    brands = request.GET.getlist('brand[]')

    allProducts = Product.objects.all().order_by('-id').distinct()
    if len(categories) > 0:
        allProducts = allProducts.filter(categories__id__in=categories).distinct()

    if len(brands) > 0:
        allProducts = allProducts.filter(brand__id__in=brands).distinct()


    t = render_to_string('ajax/shop.html', {'product': allProducts})

    return JsonResponse({'data': t})


def ProductDetail(request,slug):
    product = Product.objects.filter(slug = slug)

    if product.exists():
        product = Product.objects.get(slug = slug)
    else:
        return redirect('404')
        
    context = {
        'product' : product,
    }
    return render(request, 'product/product_detail.html', context)

def Error404(request):
    return render(request,'error404/error404.html')


def UpcomingProductDetail(request,slug):
    up_product = UpcomingProduct.objects.filter(slug = slug)

    if up_product.exists():
        up_product = UpcomingProduct.objects.get(slug = slug)
    else:
        return redirect('404')
        
    context = {
        'up_product' : up_product,
    }
    return render(request, 'product/upcoming.html', context)

def MyAccount(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Email or Password")
            return redirect('login')
        

    return render(request, 'registration/login.html')

def MyAccountSignup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            messages.error(request, "Username Already Exists")
            return redirect('handlesignup')
        
        if User.objects.filter(email = email).exists():
            messages.error(request, "Email already Exists")
            return redirect('handlesignup')

        user = User(
            username = username,
            email = email,
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account Created Successfully")
        return redirect('login')
    else:
        return render(request, 'registration/signup.html')

   

@login_required(login_url='/account/login')
def Profile(request):
    return render(request, 'profile/profile.html')


@login_required(login_url='/accounts/login/')
def ProfileUpdate(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        

        if password != None and password != "":
            user.set_password(password)
        user.save()
        return  redirect('profile')
    

    