from django.shortcuts import render,get_object_or_404,redirect
from .form import ProductForm
from .models import Product


def product_list_view(request):
    obj=Product.objects.all()
    return render(request,'products/article_list.html',{'obj':obj})


def product_detail_view(request,id):
    obj=Product.objects.get(id=id)
    return render(request,'products/article_detail.html',{'obj':obj})


def product_create_view(request):
    form=ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    return render(request,'products/create.html',{'form':form})


def product_update_view(request,id):
    obj=Product.objects.get(id=id)
    form = ProductForm(instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    return render(request,'products/update.html',{'form':form})


def product_delete_view(request,id):
    obj=get_object_or_404(Product,id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('../')
    return render(request,'products/delete.html',{'obj':obj})