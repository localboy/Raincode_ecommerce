from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm

def home(request):
    title= "Welcome"
    # if request.user.is_authenticated():
    #     title = "Welcome $s" %(request.user)

    form = SignUpForm(request.POST or None)
    context = {
        "template_title":title,
        "form":form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")

        instance.save()
        context = {
            "title":"Thank you %s"%(full_name)
        }
    return render(request, "home.html", context)