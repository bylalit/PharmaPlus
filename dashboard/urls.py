from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('login/', views.admin_login, name='dashboard_login'),
    path('products/', views.products_list, name='dashboard_products'),
    path('products/add/', views.product_add, name='dashboard_product_add'),
    path('products/edit/<int:id>/', views.product_edit, name='dashboard_product_edit'),
    path('categories/', views.categories_list, name='dashboard_categories'),
    path('categories/edit/<int:id>/', views.category_update, name='dashboard_category_update'),
    path('orders/', views.orders_list, name='dashboard_orders'),
    path('orders/<int:id>/', views.order_detail, name='dashboard_order_detail'),
    path('users/', views.users_list, name='dashboard_users'),
    path('profile/', views.profile, name='dashboard_profile'),
    path('settings/', views.settings, name='dashboard_settings'),
]
