"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core.views import Base,Home,ProductDetail,Error404,UpcomingProductDetail,MyAccount,MyAccountSignup,Profile,ProfileUpdate,AboutUs,ContactUs,BlogView,BlogDetail,Faq,Shop,filter_data

urlpatterns = [

    #404 error page
    path('404',Error404, name='404'),

    
    path('admin/', admin.site.urls),
    path('base/', Base,name='base'),
    path('',Home, name='home'),
    path('about',AboutUs, name="about"),
    path('contact',ContactUs, name='contact'),
    path('blog', BlogView, name='blogs'),
    path('faq',Faq, name='faq'),
    
    path('blog/<slug:slug>',BlogDetail, name='blog_detail'),
    path('shop',Shop, name='shop'),
    path('shop/filter-data',filter_data,name="filter-data"),

    path('product/<slug:slug>',ProductDetail, name='product_detail'),
    path('products/<slug:slug>',UpcomingProductDetail, name='up_product_detail'),
    path('account/login',MyAccount, name='handlelogin'),
    path('account/register',MyAccountSignup, name='handlesignup'),
    path('account/profile',Profile, name='profile'),
    path('account/profile/update', ProfileUpdate, name='profile_update'),
    
    path('accounts/', include('django.contrib.auth.urls'))


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
