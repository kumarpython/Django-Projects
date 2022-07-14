from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from .forms import ProductForm, RawProductForm


def product_create_view(request):
    # form = RawProductForm(request.POST)
    form = ProductForm(request.POST or None)
    if form.is_valid():
        # Product.objects.create(**form.cleaned_data)
        form.save()
        form = ProductForm()
        # form = RawProductForm()

    context = {'form' : form}
    return render(request,'products/product_create.html',context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {'object_list':queryset}
    return render(request,'products/product_list.html',context)


def product_detail_view(request,ID):
    # obj=Product.objects.get(id=id)
    obj=get_object_or_404(Product,id=ID)
    context={'title' : obj.title ,
             'description'  : obj.description,
             'price' : obj.price}
    return render(request,'products/product_detail.html',context)


def product_edit_view(request,ID):
    obj=get_object_or_404(Product,id=ID)
    form = ProductForm(request.POST or None, initial=obj)
    if form.is_valid():
        form.save()
    context = {'form' : form}
    return render(request,'products/product_detail.html',context)


def product_delete_view(request,ID):
    obj = get_object_or_404(Product, id=ID)
    context = {'obj':obj}
    if request.POST:
            obj.delete()
            return redirect('product-list')
    return render(request, 'products/product_delete.html',context)