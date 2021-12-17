from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('about',views.about,name='about'),
    path('products',views.product,name='products'),
    path('contact',views.contact,name='contact'),
    path('index',views.index,name='index'),
    path('mycart',views.mycart,name='mycart'),
    path('register_user',views.register_user,name='register_user'),
    path('logout',views.logout,name='logout'),
    path('user_login',views.user_login,name='user_login'),
    path('details',views.details,name='details'),
    path('addtocart',views.addtocart,name='addtocart'),
    path('success',views.success,name='success'),
]