from django.urls import path
from WebApp import views

urlpatterns=[
    path('Home/',views.home_page,name="home_page"),
    path('About/',views.about_page,name="about_page"),
    path('Our_Products/',views.products,name="products"),
    path('Services/',views.services,name="services"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('filtered_page/<cat_name>',views.filtered_page,name="filtered_page"),
    path('single_item/<int:item_id>',views.single_item,name="single_item"),
    path('sign_up/',views.sign_up,name="sign_up"),
    path('',views.sign_in,name="sign_in"),
    path('save_signup/',views.save_signup,name="save_signup"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('checkout/',views.checkout,name="checkout"),
    path('save_checkout/',views.save_checkout,name="save_checkout"),
    path('payment/',views.payment,name="payment"),

]