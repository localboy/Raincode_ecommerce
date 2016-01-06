from django.contrib import messages
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import VariationInventoryFormSet
from .models import Product, Variation, Category


class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()
    # template_name = "products/product_list.html"

class CategoryDetailView(DetailView):
    model = Category
    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        obj = self.get_object()
        product_set = obj.product_set.all()
        # default_products = obj.default_category.all()
        # products = ( product_set | default_products ).distinct()
        products = (product_set)
        context["products"]=products
        return context


class VariationListView(ListView):
    model = Variation
    # queryset = Product.objects.filter(active=True)-----Filtr for active product using builtin queryset.
    queryset = Variation.objects.all()  #Filter active product(active = True) using model manager

    def get_context_data(self,*args, **kwargs):
        context = super(VariationListView, self).get_context_data(*args, **kwargs)
        context["formset"] = VariationInventoryFormSet(queryset=self.get_queryset())
        return context

    def get_queryset(self, *args, **kwargs):
        product_pk = self.kwargs.get("pk")
        if product_pk:
            product = get_object_or_404(Product, pk=product_pk)
            querset = Variation.objects.filter(product=product)
        return querset

    def post(self, request, *args, **kwargs):
        formset = VariationInventoryFormSet(request.POST, request.FILES)
        print request.POST
        if formset.is_valid():
            formset.save(commit=False)
            for form in formset:
                new_item= form.save(commit=False)
                if new_item.title:
                    product_pk = self.kwargs.get("pk")
                    product = get_object_or_404(Product, pk=product_pk)
                    new_item.product = product
                    new_item.save()
            messages.success(request, "Your inventory and pricing hase been updated.")
            return redirect("products:product_list")
        raise Http404

class ProductListView(ListView):
    model = Product
    # queryset = Product.objects.filter(active=True)-----Filtr for active product using builtin queryset.
    queryset = Product.objects.all()  #Filter active product(active = True) using model manager
    def get_context_data(self,*args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
            try:
                qs2 = self.model.objects.filter(
                    Q(price=query)
                )
                qs =(qs | qs2).distinct()
            except:
                pass
        return qs


import random
class ProductDetailView(DetailView):
    model = Product
    def get_context_data(self, *args, **kwargs):
        contex = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        instance = self.get_object()
        contex["related"] = sorted(Product.objects.get_related(instance)[:6], key=lambda x:random.random())
        return contex

def product_detail_view_func(request, id):
    product_instance = get_object_or_404(Product, id=id)
    try:
        product_instance = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    except:
        raise Http404
    template = "products/product_detail.html"
    context = {
        "object":product_instance
    }
    return render(request, template, context)