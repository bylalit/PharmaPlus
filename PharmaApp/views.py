from django.shortcuts import render

CATEGORIES = [
    {"id": 1, "name": "Prescription Medicines", "image": "/static/images/cat-prescription.svg"},
    {"id": 2, "name": "Vitamins & Supplements", "image": "/static/images/cat-vitamins.svg"},
    {"id": 3, "name": "Personal Care", "image": "/static/images/cat-personal.svg"},
    {"id": 4, "name": "First Aid", "image": "/static/images/cat-firstaid.svg"},
]

PRODUCTS = [
    {
        "id": 1, "name": "Amoxicillin 500mg", "price": 12.99, "category": "Prescription Medicines",
        "image": "/static/images/product_amoxicillin.jpg", "rating": 4.8, "reviews": 124,
        "description": "Used to treat a variety of bacterial infections."
    },
    {
        "id": 2, "name": "Vitamin C 1000mg", "price": 15.99, "category": "Vitamins & Supplements",
        "image": "/static/images/product_vitaminc.jpg", "rating": 4.9, "reviews": 340,
        "description": "Daily supplement to boost your immune system."
    }
]

CART_ITEMS = [
    {"id": 1, "product": PRODUCTS[1], "quantity": 2, "total": 31.98}
]

CART_SUMMARY = {"subtotal": 31.98, "tax": 2.00, "shipping": 5.00, "total": 38.98}

FAQ_LIST = [{"question": "Q?", "answer": "A."}]
TESTIMONIALS = [{"name": "Sarah", "text": "Great!", "rating": 5}]

def index(request):
    return render(request, 'frontend/index.html', {"products": PRODUCTS, "categories": CATEGORIES})

def products(request):
    return render(request, 'frontend/products.html', {"products": PRODUCTS, "categories": CATEGORIES})

def product_detail(request, id):
    product = next((p for p in PRODUCTS if p["id"] == id), None)
    return render(request, 'frontend/product_detail.html', {"product": product})

def cart(request):
    return render(request, 'frontend/cart.html', {"cart_items": CART_ITEMS})

def checkout(request):
    return render(request, 'frontend/checkout.html', {"cart_items": CART_ITEMS, "summary": CART_SUMMARY})

def login_view(request):
    return render(request, 'frontend/login.html')

def signup_view(request):
    return render(request, 'frontend/signup.html')

def about(request):
    return render(request, 'frontend/about.html', {"testimonials": TESTIMONIALS, "faqs": FAQ_LIST})

def contact(request):
    return render(request, 'frontend/contact.html')
