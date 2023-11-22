from site import USER_BASE
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.conf import settings
from .forms import *
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "scoop/main.html")

@login_required(redirect_field_name='login')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Get the user's email or use a default email
            from_email = request.user.email if request.user.email else 'noreply@example.com'

            # Replace with your actual email address
            to_email = ['sitebyaza@gmail.com']

            # Send email
            subject = 'Contact Form'
            message = f'Name: {name}\nEmail: {email}\nMessage: {message}'
            
            send_mail(subject, message, from_email, to_email, fail_silently=False)

            return redirect('home')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'scoop/contact.html', {'form': form})

def collections(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'scoop/products/products.html', context)

@login_required(redirect_field_name='login')
def productview(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'scoop/products/view.html', context)

@login_required(redirect_field_name='login')    
def collection_detail(request, collection_id):
    collection = get_object_or_404(pk=collection_id)
    context = {'collection': collection,}
    return render(request, "scoop/products/view.html", context)

@login_required(redirect_field_name='login')
def sale_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            Product.objects.create(
                name = cd['name'],
                image = cd['image'],
                description = cd['description'],
                author=request.user 
                )
            return redirect(to='collections')
    else:
        form = ProductForm()
    context = {
        'form':form
    }
    return render(request, "scoop/create.html", context)


@login_required(redirect_field_name='login')
def sale_delete(request, pk):
    products = Product.objects.get(id=pk)
    products.delete()
    return redirect(to='collections')

@login_required(redirect_field_name='login')
def sale_update(request, pk):
    products = Product.objects.get(id=pk)
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=products,files=request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            author = request.user
            products.name = name
            products.image = image
            products.description = description
            products.save()
            return redirect(to='collections')
    else:
        form = ProductForm()
    context = {
        'form':form
    }
    return render(request, "scoop/update.html",context)