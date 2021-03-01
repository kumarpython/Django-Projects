from .models import Product
from django.shortcuts import render, redirect
from .forms import ProductForm


def product_all(request):
    queryset=Product.objects.all()
    context={'objects_all':queryset}
    return render(request,'products/home.html',context)


def product_detail_view(request,id):
    obj=Product.objects.get(id=id)
    context={
        'title':obj.title,
        'description':obj.description,
        'price':obj.price,
    }
    return render(request,'products/details.html',context)


def product_create_view(request):
    obj = Product.objects.get(id=1)
    form=ProductForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {'form': form}
    return render(request,'products/product_create.html',context)


def product_delete_view(request,id):
    obj=Product.objects.get_object_or_404(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('../')
    context={
        'title':obj.title,
        'description':obj.description,
        'price':obj.price,
    }
    return render(request,'products/details.html',context)



# def product_create_view(request):
#     obj = Product.objects.get(id=1)
#     initial={'title':"Abc",'description':'My Desc','price':100}
#     form = RawProductForm()
#     if request.method=='POST':
#         form=RawProductForm(request.POST OR None,instance=obj)
#         if form.is_valid():
#             print(form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {'form': form}
#     obj = Product.objects.get(id=1)
#     return render(request,'products/product_create.html',context)