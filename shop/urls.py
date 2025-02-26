from django.urls import path,include
from . import views as shop_views

urlpatterns = [
    path('',shop_views.home , name='home'),
    path('cart/',shop_views.cart , name='cart'),
    path('login/',shop_views.login_user ,name='login'),
    path('signup/',shop_views.signup_user ,name='signup'),
    path('logout/',shop_views.logout_user ,name='logout')
]
