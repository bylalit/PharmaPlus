from django.shortcuts import render

def index(request): return render(request, 'index.html')
def products(request): return render(request, 'products.html')
def product_detail(request): return render(request, 'product_detail.html')
def cart(request): return render(request, 'cart.html')
def checkout(request): return render(request, 'checkout.html')
def login_view(request): return render(request, 'login.html')
def signup_view(request): return render(request, 'signup.html')
def about(request): return render(request, 'about.html')
def contact(request): return render(request, 'contact.html')
