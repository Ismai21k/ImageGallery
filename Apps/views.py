from django.shortcuts import render, get_object_or_404, redirect
from .models import Product  # Import the Product model which represents our products table in the database.
from .forms import ProductForm  # Import the ProductForm to handle product creation and editing.

# View to list all products.
def product(request):
    # Retrieve all products from the database.
    products = Product.objects.all()
    # Render the 'index.html' template with the list of products.
    return render(request, 'Apps/index.html', {'products': products})

# View to add a new product.
def add_product(request):
    if request.method == 'POST':
        # Create a form instance with data from the POST request and handle file uploads.
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():  # Validate the form data.
            form.save()  # Save the new product record to the database.
            # Redirect to the product list view after successfully saving.
            return redirect('product')
    else:
        # For GET requests, create an empty form for the user to fill out.
        form = ProductForm()
    
    # Render the 'add_product.html' template with the form context.
    return render(request, 'Apps/add_product.html', {'form': form})

# View to edit an existing product.
def product_edit(request, pk):
    # Retrieve the product by primary key (pk) or return a 404 error if not found.
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        # Create a form instance with POST data and file uploads, pre-populated with the product instance.
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():  # Validate the form data.
            form.save()  # Save the updated product data to the database.
            # Redirect back to the product list view after saving changes.
            return redirect('product')
    else:
        # For GET requests, populate the form with the existing product data.
        form = ProductForm(instance=product)
        
    # Render the 'product_edit.html' template with both the form and the product instance.
    return render(request, 'Apps/product_edit.html', {'form': form, 'product': product})

# View to delete a product.
def delete_product(request, pk):
    # Retrieve the product to be deleted by primary key (pk) or return a 404 error if not found.
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        # Delete the product from the database.
        product.delete()
        # Redirect to the product list view after deletion.
        return redirect('product')
    
    # Render a confirmation template 'delete_product.html' with the product context.
    return render(request, 'Apps/delete_product.html', {'product': product})
