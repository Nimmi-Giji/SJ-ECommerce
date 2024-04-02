from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm, CategoryForm

# Read Product
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

# Update Product
def product_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/product_update.html', {'form': form})

# Delete Product
def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'store/product_delete.html', {'product': product})

# Read (View) Category
def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'store/category_detail.html', {'category': category})

def category_update(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail', category_id=category_id)
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'store/category_update.html', {'form': form, 'category': category})

# Delete Category
def category_delete(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    
    if request.method == 'POST':
        category.delete()
        return redirect('home') 
    return render(request, 'store/category_delete.html', {'category': category})

# Read (View) Review
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'store/review_detail.html', {'review': review})

# Update Review
def review_update(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_detail', review_id=review_id)
    else:
        form = ReviewForm(instance=review)
    
    return render(request, 'store/review_update.html', {'form': form, 'review': review})

# Delete Review
def review_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    
    if request.method == 'POST':
        review.delete()
        return redirect('home') 
    
    return render(request, 'store/review_delete.html', {'review': review})

# Product Create View
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)

# Home Page
def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})