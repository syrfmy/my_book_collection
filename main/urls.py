from django.urls import path
from main.views import show_main, create_product, show_xml, \
        show_json, show_json_by_id, show_xml_by_id, show_book, \
        register, login_user, logout_user, add_stock ,reduce_stock, delete_product, change_amount

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('show_book', show_book, name='show_book'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('change_amount/', change_amount, name='change_amount'),
    path('product/add_stock/<int:product_id>/', add_stock, name='add_stock'),
    path('product/reduce_stock/<int:product_id>/', reduce_stock, name='reduce_stock'),
    path('product/delete/<int:product_id>/', delete_product, name='delete_product'),
]