from django.shortcuts import render

# Dummy Data for Dashboard
DUMMY_PRODUCTS = [
    {"id": 1, "name": "Vitamin C 1000mg", "category": "Vitamins", "price": 15.99, "stock": 120, "image": "https://via.placeholder.com/50"},
    {"id": 2, "name": "Aspirin 500mg", "category": "Medicines", "price": 8.50, "stock": 5, "image": "https://via.placeholder.com/50"},
    {"id": 3, "name": "Bandages Pack", "category": "First Aid", "price": 4.50, "stock": 300, "image": "https://via.placeholder.com/50"},
]

DUMMY_ORDERS = [
    {"id": 1024, "customer": "John Doe", "date": "2026-04-18", "status": "Shipped", "total": 41.48},
    {"id": 1025, "customer": "Jane Smith", "date": "2026-04-19", "status": "Pending", "total": 120.00},
    {"id": 1026, "customer": "Alex Johnson", "date": "2026-04-15", "status": "Delivered", "total": 25.50},
]

DUMMY_USERS = [
    {"name": "Admin User", "email": "admin@pharmaplus.com", "role": "Admin", "joined": "2024-01-10"},
    {"name": "John Doe", "email": "john.doe@example.com", "role": "Customer", "joined": "2024-03-22"},
    {"name": "Jane Smith", "email": "jane@example.com", "role": "Customer", "joined": "2025-05-18"},
]

DUMMY_CATEGORIES = [
    {"id": 1, "name": "Prescription Medicines"},
    {"id": 2, "name": "Vitamins & Supplements"},
    {"id": 3, "name": "First Aid"},
]

def dashboard_home(request):
    return render(request, "backend/dashboard.html", {
        "recent_orders": DUMMY_ORDERS,
        "recent_users": DUMMY_USERS,
        "top_products": [
            {"name": "Vitamin C", "sales": 450, "price": 15.99, "image": "https://via.placeholder.com/50"},
            {"name": "Protein Powder", "sales": 320, "price": 34.99, "image": "https://via.placeholder.com/50"}
        ]
    })

def admin_login(request):
    return render(request, "backend/admin_login.html")

def products_list(request):
    return render(request, "backend/products_list.html", {"products": DUMMY_PRODUCTS})

def product_add(request):
    return render(request, "backend/product_add.html")

def product_edit(request, id):
    return render(request, "backend/product_edit.html", {"id": id})

def categories_list(request):
    return render(request, "backend/categories_list.html", {"categories": DUMMY_CATEGORIES})

def category_update(request, id):
    return render(request, "backend/category_update.html", {"id": id})

def orders_list(request):
    return render(request, "backend/orders_list.html", {"orders": DUMMY_ORDERS})

def order_detail(request, id):
    return render(request, "backend/order_detail.html", {"id": id})

def users_list(request):
    return render(request, "backend/users_list.html", {"users": DUMMY_USERS})

def profile(request):
    return render(request, "backend/profile.html")

def settings(request):
    return render(request, "backend/settings.html")
