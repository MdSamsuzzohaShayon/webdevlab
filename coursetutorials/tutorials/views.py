from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "tutorials/index.html")
    # return HttpResponse("Hello")


def about(request):
    return render(request, "tutorials/about.html")


def contact(request):
    return render(request, "tutorials/contact.html")


def tutorial_series(request):
    return render(request, "tutorials/series-tutorials.html")


def individual_tutorial(request):
    return render(request, 'tutorials/individual-tutorial.html')
