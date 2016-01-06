from django.shortcuts import render

from newsletter.forms import SignUpForm

def home(request):
    form = SignUpForm(request.POST or None)
    template = "home.html"
    context = {
        "form":form
    }
    return render(request, template, context)