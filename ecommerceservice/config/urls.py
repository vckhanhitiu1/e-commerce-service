"""ecommerceservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from rest_card import views

# import sys, os
# sys.path.append(os.path.abspath(os.path.join('..', 'gateway')))

# from gateway.views import RegistrationAPI, LoginAPI

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^rest_card-auth/', include('rest_auth.urls')),
    url(r'^rest_card-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^products',views.product_get_all),
    url(r'^product/',views.create_new_product),
    url(r'^products/(<title>)/$', views.product_get_all),
    url(r'^products/(<id>)/$', views.product_get_all),
    url(r'^products/(<price>)/$', views.product_get_all),

]
