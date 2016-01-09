from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm
from products.models import ProductFeatured, Product

def home(request):
    title= "Sign Up Now"
    # if request.user.is_authenticated():
    #     title = "Welcome $s" %(request.user)
    featured_image = ProductFeatured.objects.filter(active=True).order_by("?").first()
    products = Product.objects.all().order_by("?")[:6]
    products2 = Product.objects.all().order_by("?")[:6]
    form = SignUpForm(request.POST or None)
    context = {
        "template_title":title,
        "form":form,
        "featured_image":featured_image,
        "products":products,
        "products2":products2
    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")

        instance.save()
        context = {
            "title":"Thank you %s"%(full_name)
        }
    return render(request, "home.html", context)