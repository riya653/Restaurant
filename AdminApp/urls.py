from django.urls import path
from AdminApp import views

urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('category_page/',views.category_page,name="category_page"),
    path('save_category/',views.save_category,name="save_category"),
    path('display_category/',views.display_category,name="display_category"),
    path('edit_category/<int:cat_id>/',views.edit_category,name="edit_category"),
    path('delete_category/<int:cat_id>/',views.delete_category,name="delete_category"),
    path('update_category/<int:cats_id>/',views.update_category,name="update_category"),
    path('product_page/',views.product_page,name="product_page"),
    path('save_product/',views.save_product,name="save_product"),
    path('display_product/',views.display_product,name="display_product"),
    path('delete_product/<int:pr_id>/',views.delete_product,name="delete_product"),
    path('edit_product/<int:pro_id>/',views.edit_product,name="edit_product"),
    path('update_product/<int:pro_id>/',views.update_product,name="update_product"),
    path('Login_here/',views.admin_logo_page,name="admin_logo_page"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('contact_data/',views.contact_data,name="contact_data"),
    path('delete_contact/<int:c_id>/',views.delete_contact,name="delete_contact"),
    path('add_service/',views.add_service,name="add_service"),
    path('save_service/',views.save_service,name="save_service"),
    path('display_service/',views.display_service,name="display_service"),
    path('edit_service/<int:ser_id>/',views.display_service,name="edit_service"),
    path('delete_service/<int:ser_id>/',views.delete_service,name="delete_service"),
    path('update_service/<int:ser_id>/',views.update_service,name="update_service"),

]